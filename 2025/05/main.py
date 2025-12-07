import sys


def _parse_range(s: str) -> tuple[int, int]:
    tok = s.split("-")
    return (int(tok[0]), int(tok[1]))


lines = open(sys.argv[1]).readlines()
id_ranges = [_parse_range(it) for it in lines if "-" in it]
available_ids = [int(it) for it in lines if it.strip().isdigit()]

# Part 1
fresh = 0
for id in available_ids:
    if any(id >= min_ and id <= max_ for min_, max_ in id_ranges):
        fresh += 1

print(f"Part 1: {fresh}")
