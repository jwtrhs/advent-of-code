import sys

stones = [l for l in open(sys.argv[1]).readline().strip().split(" ")]


def blink(s: str):
    return (
        ["1"]
        if s == "0"
        else [str(int(s[: len(s) // 2])), str(int(s[len(s) // 2 :]))]
        if len(s) % 2 == 0
        else [str(int(s) * 2024)]
    )


def count_stones(*stones: str, n: int = 0) -> int:
    if n == 0:
        return len(stones)
    return sum(count_stones(*blink(stone), n=n - 1) for stone in stones)


part1 = count_stones(*stones, n=25)
print(f"Part 1: {part1}")
