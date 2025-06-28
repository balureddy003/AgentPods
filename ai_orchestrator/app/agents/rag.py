from __future__ import annotations

from typing import Any, Dict

from .base import Agent
from ..tools.rag_tool import RAGTool


class RagAgent(Agent):
    name = "rag"

    def __init__(self) -> None:
        self._tool = RAGTool()
        # preload docs for demo
        self._tool.add_document("AgentPods introduction document")

    async def run(self, task: str, context: Dict[str, Any]) -> str:
        results = self._tool.query(task, top_k=1)
        return results[0] if results else "No docs"
