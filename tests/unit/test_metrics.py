from src.core.metrics import semantics_per_joule


def test_spj_basic() -> None:
    assert semantics_per_joule(10.0, 2.0) == 5.0


def test_spj_non_positive_energy() -> None:
    assert semantics_per_joule(10.0, 0.0) == 0.0
