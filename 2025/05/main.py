import itertools
import sys


def _parse_range(s: str) -> tuple[int, int]:
    tok = s.split("-")
    return (int(tok[0]), int(tok[1]))


lines = open(sys.argv[1]).readlines()
id_ranges = set([_parse_range(it) for it in lines if "-" in it])
available_ids = set([int(it) for it in lines if it.strip().isdigit()])

# Part 1
fresh = 0
for id in available_ids:
    if any(id >= min_ and id <= max_ for min_, max_ in id_ranges):
        fresh += 1

print(f"Part 1: {fresh}")


def _overlap(id1: tuple[int, int], id2: tuple[int, int]) -> bool:
    if id1[0] > id2[1]:
        return False

    if id1[1] < id2[0]:
        return False

    return True


def _collapse(ids: set[tuple[int, int]]) -> set[tuple[int, int]]:
    for id1, id2 in itertools.combinations(ids, 2):
        if _overlap(id1, id2):
            return ids.difference(set([id1, id2])).union(
                set([(min(id1[0], id2[0]), max(id1[1], id2[1]))])
            )

    return ids


def _count_valid_ids(ids: set[tuple[int, int]]) -> int:
    return sum([id[1] - id[0] + 1 for id in ids])


collapsed_ids = id_ranges
while True:
    next_ids = _collapse(collapsed_ids)
    if next_ids == collapsed_ids:
        break
    collapsed_ids = next_ids

print(f"Part 2: {_count_valid_ids(collapsed_ids)}")
