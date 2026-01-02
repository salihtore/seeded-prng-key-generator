# RNG Key Generator

Bu proje, dışarıdan verilen bir **seed (tohum)** değeri ile deterministik olarak
**pseudo-random** sayı dizisi üreten bir generator (PRNG) ve bu diziden
**anahtar (key) byte dizisi** türeten bir örnektir.

## Amaç
- Anahtar kod içinde sabit olarak tutulmaz.
- Anahtar, yalnızca **seed + generator algoritması** ile **runtime**'da üretilir.
- Aynı seed her zaman aynı anahtarı üretir (deterministik).

> Not: Bu PRNG ders/ödev amaçlıdır. Kriptografik güvenlik iddiası yoktur.

## Algoritma
- PRNG: XorShift128+
- Seed yayma/karıştırma: SplitMix64 (başlangıç state türetmek için)

Akış:
`seed -> PRNG -> byte stream -> key (length byte)`

## Kurulum
Python 3.10+ yeterlidir. Ek bağımlılık yoktur.

## Kullanım

### Hex çıktısı (default)
```bash
python -m src.cli --seed 42 --len 32 --format hex
