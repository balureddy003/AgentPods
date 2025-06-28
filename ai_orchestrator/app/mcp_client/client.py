from __future__ import annotations

from typing import Any

import httpx

from ..config import get_settings


class MCPClient:
    """Client for the MCP Gateway."""

    def __init__(self) -> None:
        settings = get_settings()
        self._base_url = settings.mcp_url
        self._client = httpx.AsyncClient(base_url=self._base_url)

    async def call(self, payload: Any) -> Any:
        resp = await self._client.post("/call", json=payload)
        resp.raise_for_status()
        return resp.json()
