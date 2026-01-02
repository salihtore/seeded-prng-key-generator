# src/keygen.py
from __future__ import annotations

import base64
from dataclasses import dataclass

from .prng import XorShift128Plus


@dataclass(frozen=True)
class KeyMaterial:
    seed: int
    length: int
    raw: bytes

    def hex(self) -> str:
        return self.raw.hex()

    def b64(self) -> str:
        return base64.b64encode(self.raw).decode("ascii")


def derive_key(seed: int, length: int = 32) -> KeyMaterial:
    """
    Seed -> PRNG -> length byte anahtar.
    Varsayılan 32 byte (256-bit) üretiyoruz.
    """
    if length <= 0:
        raise ValueError("length > 0 olmalı")

    rng = XorShift128Plus(seed)
    raw = rng.next_bytes(length)
    return KeyMaterial(seed=seed, length=length, raw=raw)
