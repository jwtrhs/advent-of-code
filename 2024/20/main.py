import collections
import itertools
import sys
import typing

Position = tuple[int, int]
Map = dict[Position, str]
Path = list[Position]

DEBUG = False

map_: Map = {}
with open(sys.argv[1]) as f:
    lines = f.readlines()
    for y, row in enumerate(lines):
        if not row.strip():
            continue
        for x, v in enumerate(row.strip()):
            map_[(x, y)] = v


def print_map(map_: Map, path: Path | None = None):
    path = path or []
    width = max(x for x, _ in map_.keys()) + 1
    height = max(y for _, y in map_.keys()) + 1
    line = "\n".join(
        "".join("0" if (x, y) in path else map_[(x, y)] for x in range(0, width))
        for y in range(0, height)
    )
    print(f"{line}\n")


def shortest_path(map_: Map, start: Position, end: Position) -> Path:
    if DEBUG:
        print_map(map_)
    paths: list[list[Position]] = [[start]]
    visited: dict[Position, int] = {}
    solution: list[Position] | None = None
    while paths and not solution:
        path = paths.pop(0)
        if DEBUG:
            print_map(map_, path)
        x, y = path[-1]
        if (x, y) == end:
            solution = path
            break
        moves: list[Position] = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        ]
        for move in moves:
            if move not in map_ or move in path or map_[move] not in "S.E":
                continue
            new_path = path + [move]
            if move in visited and visited[move] <= len(new_path):
                continue
            visited[move] = len(new_path)
            paths.append(new_path)
    if not solution:
        raise RuntimeError
    return solution


def shortcuts(
    maps_: Map, path: Path, max_distance: int
) -> typing.Generator[int, None, None]:
    for i, a in enumerate(path):
        for j, b in enumerate(path[i + 1 :]):
            path_distance = j + 1
            direct_distance = abs(b[0] - a[0]) + abs(b[1] - a[1])
            if direct_distance < path_distance and direct_distance <= max_distance:
                yield path_distance - direct_distance


start = next(p for p, v in map_.items() if v == "S")
end = next(p for p, v in map_.items() if v == "E")
path = shortest_path(map_, start, end)
print(
    f"Part 1: {sum(1 if shortcut >= 100 else 0 for shortcut in shortcuts(map_, path, 2))}"
)
print(
    f"Part 2: {sum(1 if shortcut >= 100 else 0 for shortcut in shortcuts(map_, path, 20))}"
)
