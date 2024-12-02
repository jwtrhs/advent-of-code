import itertools
import sys


def read_input(path: str) -> list[list[int]]:
    with open(path) as f:
        lines = f.readlines()
    levels = [it.strip().split(" ") for it in lines]
    return [[int(it2) for it2 in it1] for it1 in levels]


def increasing(levels: list[int]):
    for a, b in itertools.pairwise(levels):
        if a >= b:
            return False
    return True


def decreasing(levels: list[int]):
    for a, b in itertools.pairwise(levels):
        if a <= b:
            return False
    return True


def difference(levels: list[int]):
    for a, b in itertools.pairwise(levels):
        diff = abs(a - b)
        if diff < 1 or diff > 3:
            return False
    return True


if __name__ == "__main__":
    data = read_input(sys.argv[1])

    num_safe = 0
    for levels in data:
        if (increasing(levels) or decreasing(levels)) and difference(levels):
            num_safe += 1
    print(f"Part A: {num_safe}")

    num_safe = 0
    for levels in data:
        for permutation in itertools.combinations(levels, r=len(levels) - 1):
            if (increasing(permutation) or decreasing(permutation)) and difference(
                permutation
            ):
                num_safe += 1
                break
    print(f"Part B: {num_safe}")
