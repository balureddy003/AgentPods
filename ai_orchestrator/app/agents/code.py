from __future__ import annotations

from typing import Any, Dict

from .base import Agent
from ..llm_provider.openai_provider import LLMProvider


class CodeAgent(Agent):
    name = "code"

    def __init__(self) -> None:
        self._llm = LLMProvider()

    async def run(self, task: str, context: Dict[str, Any]) -> str:
        prompt = f"Write code for: {task}"
        return await self._llm.generate(prompt)
