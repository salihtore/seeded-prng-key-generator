# src/prng.py
from __future__ import annotations

MASK64 = (1 << 64) - 1


def _splitmix64(seed: int) -> int:
    """
    SplitMix64: 64-bit seed'i karıştırmak için kullanılır.
    XorShift'in başlangıç state'lerini seed'den türetmekte işimize yarar.
    """
    x = (seed + 0x9E3779B97F4A7C15) & MASK64
    x = (x ^ (x >> 30)) * 0xBF58476D1CE4E5B9 & MASK64
    x = (x ^ (x >> 27)) * 0x94D049BB133111EB & MASK64
    x = x ^ (x >> 31)
    return x & MASK64


class XorShift128Plus:
    """
    Deterministik pseudo-random generator.
    Aynı seed -> aynı sayı dizisi üretir.

    Not: Bu PRNG kriptografik RNG değildir. Ders/ödev için uygundur.
    """

    def __init__(self, seed: int):
        if not isinstance(seed, int):
            raise TypeError("seed int olmalı")

        # state[0], state[1] seed'den türetilir
        s0 = _splitmix64(seed)
        s1 = _splitmix64(s0)

        # state'in "tamamı sıfır" olmasını engelle (çok nadir ama önlem)
        if s0 == 0 and s1 == 0:
            s1 = 0x1

        self._s0 = s0
        self._s1 = s1

    def next_u64(self) -> int:
        """
        0..2^64-1 arası 64-bit pseudo-random üretir.
        """
        s1 = self._s0
        s0 = self._s1
        self._s0 = s0

        s1 ^= (s1 << 23) & MASK64
        s1 ^= (s1 >> 17) & MASK64
        s1 ^= s0 & MASK64
        s1 ^= (s0 >> 26) & MASK64

        self._s1 = s1 & MASK64
        out = (self._s1 + s0) & MASK64
        return out

    def next_bytes(self, n: int) -> bytes:
        """
        n adet byte üretir.
        """
        if n < 0:
            raise ValueError("n >= 0 olmalı")

        out = bytearray()
        while len(out) < n:
            x = self.next_u64()
            # 8 byte'lık bloklar halinde ekle (little-endian)
            out.extend(x.to_bytes(8, "little"))
        return bytes(out[:n])
