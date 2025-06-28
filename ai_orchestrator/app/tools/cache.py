from __future__ import annotations

from typing import Any

import redis.asyncio as redis

from ..config import get_settings


class Cache:
    """Simple Redis cache."""

    def __init__(self) -> None:
        settings = get_settings()
        self._redis = redis.from_url(settings.redis_url, decode_responses=True)

    async def get(self, key: str) -> Any:
        return await self._redis.get(key)

    async def set(self, key: str, value: Any, expire: int | None = None) -> None:
        await self._redis.set(key, value, ex=expire)
