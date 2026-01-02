# src/cli.py
from __future__ import annotations

import argparse
import sys

from .keygen import derive_key


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="rng-key-generator",
        description="Seed tabanlı PRNG ile deterministik anahtar üretimi",
    )
    p.add_argument("--seed", required=True, type=int, help="Tohum değeri (int)")
    p.add_argument("--len", default=32, type=int, help="Anahtar uzunluğu (byte)")
    p.add_argument(
        "--format",
        choices=["hex", "b64", "raw"],
        default="hex",
        help="Çıktı formatı",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)

    km = derive_key(seed=args.seed, length=args.len)

    if args.format == "hex":
        print(km.hex())
    elif args.format == "b64":
        print(km.b64())
    else:
        # raw bytes'ı terminale basmak riskli; yine de istenirse:
        sys.stdout.buffer.write(km.raw)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
