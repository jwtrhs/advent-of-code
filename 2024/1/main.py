import collections
import functools
import sys


def read_input(path: str) -> tuple[list[int], list[int]]:
    with open(path) as f:
        lines = f.readlines()

    numbers = [it.strip().split("   ") for it in lines]
    list1 = [int(it[0]) for it in numbers]
    list2 = [int(it[1]) for it in numbers]
    list1.sort()
    list2.sort()

    return list1, list2


if __name__ == "__main__":
    list1, list2 = read_input(sys.argv[1])

    # Part 1
    distance = functools.reduce(
        lambda total, item: total + abs(item[0] - item[1]), zip(list1, list2), 0
    )
    print(f"Part 1 Answer (cumulative distance): {distance}")

    # Part 2
    def _accumulate(frequency, item):
        frequency[item] += 1
        return frequency

    list2_frequency = functools.reduce(_accumulate, list2, collections.defaultdict(int))
    similarity = functools.reduce(
        lambda total, item: total + item * list2_frequency[item], list1, 0
    )
    print(f"Part 2 Answer(similarity score): {similarity}")
