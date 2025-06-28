from __future__ import annotations

from typing import Any, Dict, List

from .db.marketplace_store import MarketplaceStore


class Marketplace:
    """Simple marketplace backed by MongoDB."""

    def __init__(self) -> None:
        self._store = MarketplaceStore()

    async def publish(self, item: Dict[str, Any]) -> str:
        return await self._store.publish(item)

    async def list_items(self) -> List[Dict[str, Any]]:
        return await self._store.list_items()
