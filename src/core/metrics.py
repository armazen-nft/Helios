"""Energy-aware semantic metrics."""


def semantics_per_joule(semantic_value: float, energy_joules: float) -> float:
    """Calculate semantic efficiency as bits per joule."""
    if energy_joules <= 0:
        return 0.0
    return semantic_value / energy_joules
