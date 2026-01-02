# tests/test_vectors.py
from src.keygen import derive_key


def test_same_seed_same_key():
    k1 = derive_key(12345, 32).hex()
    k2 = derive_key(12345, 32).hex()
    assert k1 == k2


def test_diff_seed_diff_key():
    k1 = derive_key(1, 32).hex()
    k2 = derive_key(2, 32).hex()
    assert k1 != k2
