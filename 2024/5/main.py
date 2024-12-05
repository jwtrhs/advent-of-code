import collections
import itertools
import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    rules = set()
    updates = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if "|" in line:
            rules.add(tuple(line.split("|")))
        else:
            updates.append(line.split(","))

    result = 0
    for update in updates:
        combinations = itertools.combinations(update, r=2)
        if all(it in rules for it in combinations):
            result += int(update[len(update) // 2])
    assert result == 5651
    print(f"Part A: {result}")
