"""FastAPI wrapper for Helios core capabilities."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from core.bridge import Bridge
from core.metrics import semantics_per_joule

app = FastAPI(title="Helios SBL API", version="0.1.0")
_bridge = Bridge()


class EncodeRequest(BaseModel):
    text: str = Field(default="", description="Input text to encode")
    source_model: str = Field(default="generic", description="Producer model identifier")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "operational", "spj": "available"}


@app.post("/api/encode")
def encode_text(payload: EncodeRequest) -> dict[str, object]:
    ideogram = _bridge.encode(source_model=payload.source_model, data=payload.text)
    energy = max(len(payload.text), 1)
    spj = semantics_per_joule(semantic_value=float(len(payload.text)), energy_joules=float(energy))

    response = ideogram.to_dict()
    response["metrics"] = {**response["metrics"], "spj": spj}
    return response
