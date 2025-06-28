from __future__ import annotations

from typing import Any, Dict, List

from motor.motor_asyncio import AsyncIOMotorClient

from ..config import get_settings


class ChatMemory:
    """MongoDB-based chat memory store."""

    def __init__(self) -> None:
        settings = get_settings()
        self._client = AsyncIOMotorClient(settings.mongo_url)
        self._db = self._client[settings.mongo_db]
        self._col = self._db["chat_memory"]

    async def add_message(self, pod_id: str, role: str, content: str) -> None:
        await self._col.insert_one({"pod_id": pod_id, "role": role, "content": content})

    async def get_messages(self, pod_id: str) -> List[Dict[str, Any]]:
        cursor = self._col.find({"pod_id": pod_id}).sort("_id")
        return [doc async for doc in cursor]
