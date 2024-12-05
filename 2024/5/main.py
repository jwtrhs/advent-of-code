import itertools
import sys


def _update_correct(update: list[str], rules: set[tuple[str, str]]):
    return all(it in rules for it in itertools.combinations(update, r=2))


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    rules: set[tuple[str, str]] = set()
    updates: list[list[str]] = []
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
        if _update_correct(update, rules):
            result += int(update[len(update) // 2])
    assert result == 5651
    print(f"Part A: {result}")

    result = 0
    for update in updates:
        combinations = itertools.combinations(update, r=2)
        if _update_correct(update, rules):
            continue
        fixed_update: list[str] = [update[0]]
        for u in update[1:]:
            for index in range(0, len(fixed_update) + 1):
                potential_update = list(fixed_update)
                potential_update.insert(index, u)
                if _update_correct(potential_update, rules):
                    new_update = potential_update
        assert len(update) == len(fixed_update)
        assert _update_correct(fixed_update, rules)
        result += int(fixed_update[len(fixed_update) // 2])
    assert result == 4743
    print(f"Part B: {result}")
