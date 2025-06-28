from __future__ import annotations

from typing import Any, Dict


class Agent:
    """Base class for agents."""

    name: str = "base"

    async def run(self, task: str, context: Dict[str, Any]) -> str:
        """Execute the agent task."""
        raise NotImplementedError
