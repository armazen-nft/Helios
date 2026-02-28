"""Bridge for encoding/decoding between model-specific payloads and ideograms."""

from __future__ import annotations

from .ideogram import Ideogram


class Bridge:
    """Simple deterministic bridge scaffold."""

    def encode(self, source_model: str, data: str) -> Ideogram:
        """Encode text payload into a naive deterministic ideogram embedding."""
        if not data:
            embedding = [0.0]
        else:
            chars = [ord(c) for c in data]
            embedding = [sum(chars) / len(chars), float(len(data)), float(len(set(data)))]

        return Ideogram(
            embedding=embedding,
            graph={"source_model": source_model},
            operators=["normalize", "tokenize"],
            metrics={"length": float(len(data))},
        )

    def decode(self, target_model: str, ideogram: Ideogram) -> dict[str, object]:
        """Decode ideogram into a model-friendly payload."""
        return {
            "target_model": target_model,
            "embedding": ideogram.embedding,
            "metadata": {
                "graph": ideogram.graph,
                "operators": ideogram.operators,
                "metrics": ideogram.metrics,
            },
        }
