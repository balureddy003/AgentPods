from __future__ import annotations

import numpy as np
from typing import List


class RAGTool:
    """Simple retrieval tool backed by in-memory vectors."""

    def __init__(self) -> None:
        self._docs: List[str] = []
        self._embeddings: List[np.ndarray] = []

    def add_document(self, doc: str) -> None:
        self._docs.append(doc)
        self._embeddings.append(self._embed(doc))

    def _embed(self, text: str) -> np.ndarray:
        return np.random.random(128)

    def query(self, text: str, top_k: int = 1) -> List[str]:
        if not self._docs:
            return []
        vec = self._embed(text)
        sims = [float(vec @ emb) for emb in self._embeddings]
        idxs = np.argsort(sims)[::-1][:top_k]
        return [self._docs[i] for i in idxs]
