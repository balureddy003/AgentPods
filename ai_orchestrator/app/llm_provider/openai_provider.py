from __future__ import annotations

from typing import Any, Dict


class LLMProvider:
    """Placeholder LLM provider."""

    async def generate(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
        # In production, call OpenAI or another provider
        return f"LLM response to: {prompt}"
