from __future__ import annotations

from typing import Dict, Type

from app.agents.base import Agent
from app.agents.planner import PlannerAgent
from app.agents.websearch import WebSearchAgent
from app.agents.rag import RagAgent
from app.agents.code import CodeAgent
from app.agents.mcp import MCPAgent


class AgentRegistry:
    """Registry of available agents."""

    def __init__(self) -> None:
        self._agents: Dict[str, Type[Agent]] = {
            "planner": PlannerAgent,
            "web_search": WebSearchAgent,
            "rag": RagAgent,
            "code": CodeAgent,
            "mcp": MCPAgent,
        }

    def get(self, name: str) -> Type[Agent]:
        return self._agents[name]
