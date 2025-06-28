from __future__ import annotations

from typing import List, Dict, Any

from pydantic import BaseModel


class PodConfig(BaseModel):
    agents: List[str]


class ChatRequest(BaseModel):
    message: str


class MarketplaceItem(BaseModel):
    name: str
    description: str | None = None
    metadata: Dict[str, Any] | None = None
