from core.bridge import Bridge
from core.ideogram import Ideogram


def test_ideogram_roundtrip() -> None:
    original = Ideogram(embedding=[0.1, 0.2], graph={"node": 1}, operators=["op"], metrics={"m": 1.0})
    rebuilt = Ideogram.from_dict(original.to_dict())
    assert rebuilt == original


def test_bridge_encode_decode() -> None:
    bridge = Bridge()
    ideogram = bridge.encode(source_model="gpt", data="hello")
    payload = bridge.decode(target_model="claude", ideogram=ideogram)
    assert payload["target_model"] == "claude"
    assert payload["embedding"] == ideogram.embedding
