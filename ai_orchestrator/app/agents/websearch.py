from __future__ import annotations

from typing import Any, Dict

from .base import Agent


class WebSearchAgent(Agent):
    name = "web_search"

    async def run(self, task: str, context: Dict[str, Any]) -> str:
        query = task
        # Stub web search
        return f"Search results for: {query}"
