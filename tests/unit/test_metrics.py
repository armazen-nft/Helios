from core.metrics import semantics_per_joule


def test_semantics_per_joule_positive_energy() -> None:
    assert semantics_per_joule(semantic_value=10.0, energy_joules=2.0) == 5.0


def test_semantics_per_joule_non_positive_energy() -> None:
    assert semantics_per_joule(semantic_value=10.0, energy_joules=0.0) == 0.0
