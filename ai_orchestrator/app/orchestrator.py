from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, List
import logging

from .agents.base import Agent
from .registry.registry import AgentRegistry
from .db.chat_memory import ChatMemory


def _generate_id() -> str:
    return str(uuid.uuid4())


@dataclass
class Pod:
    pod_id: str
    config: Dict[str, Any]
    memory: ChatMemory
    agents: List[Agent] = field(default_factory=list)


class Orchestrator:
    """Main orchestrator managing pods and agents."""

    def __init__(self, registry: AgentRegistry, memory: ChatMemory) -> None:
        self.registry = registry
        self.memory = memory
        self.pods: Dict[str, Pod] = {}
        self._log = logging.getLogger(self.__class__.__name__)

    async def create_pod(self, config: Dict[str, Any]) -> Pod:
        pod_id = _generate_id()
        agents = [self.registry.get(name)() for name in config.get("agents", [])]
        pod = Pod(pod_id=pod_id, config=config, memory=self.memory, agents=agents)
        self.pods[pod_id] = pod
        self._log.info("Created pod %s with agents %s", pod_id, [a.name for a in agents])
        return pod

    async def delete_pod(self, pod_id: str) -> None:
        self.pods.pop(pod_id, None)

    async def list_pods(self) -> List[Pod]:
        return list(self.pods.values())

    async def chat(self, pod_id: str, message: str) -> str:
        pod = self.pods[pod_id]
        await self.memory.add_message(pod_id, "user", message)
        context: Dict[str, Any] = {}
        result = message
        for agent in pod.agents:
            self._log.debug("Running agent %s", agent.name)
            result = await agent.run(result, context)
        await self.memory.add_message(pod_id, "assistant", result)
        return result

    async def history(self, pod_id: str) -> List[Dict[str, Any]]:
        return await self.memory.get_messages(pod_id)
