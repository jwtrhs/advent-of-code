import sys

INITIAL_SECRETS = [int(l.strip()) for l in open(sys.argv[1]) if l.strip()]


def secret_number(initial_secret: int, r: int):
    secret = initial_secret
    for _ in range(0, r):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
    return secret


part1 = sum(secret_number(it, 2000) for it in INITIAL_SECRETS)
print(f"Part 1: {part1}")
