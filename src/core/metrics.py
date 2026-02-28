"""Metrics helpers (scaffold)."""


def semantics_per_joule(semantic_information: float, joules: float) -> float:
    if joules <= 0:
        return 0.0
    return semantic_information / joules
