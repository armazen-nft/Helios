"""Core Ideogram data model (scaffold)."""

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Ideogram:
    state_vector: Dict[str, Any]
    semantic_graph: Dict[str, Any]
    operators: Dict[str, Any] = field(default_factory=dict)
    metrics: Dict[str, float] = field(default_factory=dict)
    energy: Dict[str, float] = field(default_factory=dict)
    thermodynamics: Dict[str, float] = field(default_factory=dict)
