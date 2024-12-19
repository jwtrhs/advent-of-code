import collections
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    patterns = [it.strip() for it in lines[0].split(",")]
    designs = [it.strip() for it in lines[1:] if it.strip()]


def can_be_made(design: str, patterns: list[str]) -> bool:
    towels_to_check: list[str] = [""]
    while towels_to_check:
        towel = towels_to_check.pop()
        assert design.startswith(towel)
        if towel == design:
            return True
        next_towels = [
            towel + p for p in patterns if design[len(towel) :].startswith(p)
        ]
        towels_to_check.extend(next_towels)
    return False


def count(design: str, patterns: list[str]) -> int:
    towels: dict[str, int] = {"": 1}
    while towels:
        towel, count = sorted(towels.items(), key=lambda x: len(x[0]))[0]
        if towel == design:
            return count
        next_towels = [
            towel + p for p in patterns if design[len(towel) :].startswith(p)
        ]
        for next_towel in next_towels:
            if next_towel in towels:
                towels[next_towel] += count
            else:
                towels[next_towel] = count
        del towels[towel]

    return 0


print(f"Part 1: {sum(1 if can_be_made(design, patterns) else 0 for design in designs)}")
print(f"Part 2: {sum(count(design, patterns) for design in designs)}")
