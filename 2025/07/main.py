import collections
import sys


def _get_input() -> dict[tuple[int, int], str]:
    diagram = [it.strip() for it in open(sys.argv[1]).readlines() if it.strip()]
    return {
        (x, y): diagram[y][x]
        for y in range(0, len(diagram))
        for x in range(0, len(diagram[y]))
    }


map_ = _get_input()
columns = max(it[0] for it in map_.keys())
rows = max(it[1] for it in map_.keys())
splits = 0
for y in range(1, rows):
    for x in range(0, columns):
        if map_[(x, y - 1)] in ["S", "|"] and map_[(x, y)] == ".":
            map_[(x, y)] = "|"
    for x in range(0, columns):
        if map_[(x, y - 1)] in ["S", "|"] and map_[(x, y)] == "^":
            if map_.get((x - 1, y)) == ".":
                map_[(x - 1, y)] = "|"
            if map_.get((x + 1, y)) == ".":
                map_[(x + 1, y)] = "|"
            splits += 1
print(f"Part 1: {splits}")


map_ = _get_input()
timelines: list[dict[tuple[int, int], int]] = [
    collections.defaultdict(int) for _ in range(0, rows)
]
start = next(coord for coord, value in map_.items() if value == "S")
timelines[0][start] = 1
for row in range(0, rows - 1):
    for (x, y), count in timelines[row].items():
        if map_.get((x, y + 1)) == ".":
            timelines[row + 1][(x, y + 1)] += count
        if map_.get((x, y + 1)) == "^":
            if (x - 1, y + 1) in map_:
                timelines[row + 1][(x - 1, y + 1)] += count
            if (x + 1, y + 1) in map_:
                timelines[row + 1][(x + 1, y + 1)] += count
print(f"Part 2: {sum(timelines[-1].values())}")
