import itertools
import sys
from typing import Iterable

Stone = str

stones: list[Stone] = [l for l in open(sys.argv[1]).readline().strip().split(" ")]


# Maps a tuple of (Stone, number of blinks) to a count of the number of stones
# left after that number of blinks
_cache: dict[tuple[Stone, int], int] = {}


def blink_recursive(*stones: Stone, n: int = 1) -> int:
    if n == 0:
        return len(stones)

    count = 0
    for s in stones:
        # Check cache first
        if (s, n) in _cache:
            count += _cache[(s, n)]
            continue

        # Calculate the next set of stones
        stones_ = (
            ["1"]
            if s == "0"
            else [str(int(s[: len(s) // 2])), str(int(s[len(s) // 2 :]))]
            if len(s) % 2 == 0
            else [str(int(s) * 2024)]
        )
        # Recursively call this function on the next set of stones and cache the result
        count_ = blink_recursive(*stones_, n=n - 1)
        _cache[(s, n)] = count_
        count += count_
    return count


part1 = blink_recursive(*stones, n=25)
print(f"Part 1: {part1}")
assert part1 == 202019


part2 = blink_recursive(*stones, n=75)
print(f"Part 2: {part2}")
assert part2 == 239321955280205
