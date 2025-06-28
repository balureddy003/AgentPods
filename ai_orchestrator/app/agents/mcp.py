from __future__ import annotations

from typing import Any, Dict

from .base import Agent
from ..mcp_client.client import MCPClient
from ..tools.cache import Cache


class MCPAgent(Agent):
    name = "mcp"

    def __init__(self) -> None:
        self._client = MCPClient()
        self._cache = Cache()

    async def run(self, task: str, context: Dict[str, Any]) -> str:
        cached = await self._cache.get(task)
        if cached:
            return cached
        result = await self._client.call({"task": task})
        text = str(result)
        await self._cache.set(task, text, expire=3600)
        return text
