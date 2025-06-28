from __future__ import annotations

import os
from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application settings loaded from environment."""

    mongo_url: str = Field("mongodb://mongo:27017", env="MONGO_URL")
    mongo_db: str = Field("agentpods", env="MONGO_DB")
    redis_url: str = Field("redis://redis:6379/0", env="REDIS_URL")
    mcp_url: str = Field("http://mcp:4444", env="MCP_URL")
    keycloak_url: str = Field("http://keycloak:8080", env="KEYCLOAK_URL")
    allow_all_origins: bool = Field(False, env="ALLOW_ALL_ORIGINS")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
