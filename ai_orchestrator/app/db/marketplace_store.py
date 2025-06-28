from __future__ import annotations

from typing import Any, Dict, List

from motor.motor_asyncio import AsyncIOMotorClient

from ..config import get_settings


class MarketplaceStore:
    """MongoDB collection for marketplace items."""

    def __init__(self) -> None:
        settings = get_settings()
        self._client = AsyncIOMotorClient(settings.mongo_url)
        self._db = self._client[settings.mongo_db]
        self._col = self._db["marketplace"]

    async def publish(self, item: Dict[str, Any]) -> str:
        result = await self._col.insert_one(item)
        return str(result.inserted_id)

    async def list_items(self) -> List[Dict[str, Any]]:
        cursor = self._col.find().sort("_id")
        return [doc async for doc in cursor]
