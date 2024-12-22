import collections
import itertools
import sys
import typing


INITIAL_SECRETS = [int(l.strip()) for l in open(sys.argv[1]) if l.strip()]


def secret_numbers(initial_secret: int) -> typing.Generator[int, None, None]:
    secret = initial_secret
    while True:
        yield secret
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216


def prices(initial_secret: int) -> typing.Generator[tuple[int, int], None, None]:
    for a, b in itertools.pairwise(secret_numbers(initial_secret)):
        yield b % 10, (b % 10) - (a % 10)


def sequences(
    initial_secret: int,
) -> typing.Generator[tuple[tuple[int, int, int, int], int], None, None]:
    sequence = []
    for price in prices(initial_secret):
        sequence.append(price[1])
        if len(sequence) == 4:
            yield tuple(sequence), price[0]
            sequence.pop(0)


def sequence_map(initial_secret: int, r: int) -> dict[tuple[int, int, int, int], int]:
    s: dict[tuple[int, int, int, int], int] = {}
    for sequence, price in itertools.islice(sequences(initial_secret), 0, r - 4):
        if sequence not in s:
            s[sequence] = price
    return s


part1 = sum(
    next(itertools.islice(secret_numbers(it), 2000, None)) for it in INITIAL_SECRETS
)
print(f"Part 1: {part1}")

s = collections.defaultdict(int)
for initial_secret in INITIAL_SECRETS:
    for k, v in sequence_map(initial_secret, r=2000).items():
        s[k] += v
best = next(it for it in sorted(s.items(), key=lambda x: x[1], reverse=True))
print(f"Part 2: {best[1]}")
