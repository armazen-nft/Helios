"""Ideogram representation for semantic boundary logic."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Ideogram:
    """Canonical semantic representation used across model boundaries."""

    embedding: list[float]
    graph: dict[str, Any] = field(default_factory=dict)
    operators: list[str] = field(default_factory=list)
    metrics: dict[str, float] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Serialize ideogram payload for transport and API responses."""
        return {
            "embedding": self.embedding,
            "graph": self.graph,
            "operators": self.operators,
            "metrics": self.metrics,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "Ideogram":
        """Construct an ideogram from an API payload."""
        return cls(
            embedding=list(payload.get("embedding", [])),
            graph=dict(payload.get("graph", {})),
            operators=list(payload.get("operators", [])),
            metrics=dict(payload.get("metrics", {})),
        )
