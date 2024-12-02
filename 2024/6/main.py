import sys
import typing

Map = dict[tuple[int, int], str]
Guard = tuple[int, int, str]


def _get_map() -> tuple[Map, Guard]:
    map_: Map = {}
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    guard: Guard | None = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            map_[(x, y)] = char
            if char in "^><v":
                guard = (x, y, char)
    assert guard
    return map_, guard


def _generate_obstructions(
    points: set[tuple[int, int]],
) -> typing.Generator[tuple[Map, Guard], None, None]:
    map_, guard = _get_map()
    for x, y in points:
        if map_[(x, y)] != ".":
            continue
        map_[(x, y)] = "#"

        yield map_, guard
        map_[(x, y)] = "."


def _move_guard(map_: Map, guard: Guard) -> tuple[int, int, str]:
    x, y, direction = guard
    next_guard = guard
    try:
        if direction == "^":
            next_guard = (x, y - 1, "^") if map_[(x, y - 1)] != "#" else (x, y, ">")
        elif direction == "v":
            next_guard = (x, y + 1, "v") if map_[(x, y + 1)] != "#" else (x, y, "<")
        elif direction == "<":
            next_guard = (x - 1, y, "<") if map_[(x - 1, y)] != "#" else (x, y, "^")
        elif direction == ">":
            next_guard = (x + 1, y, ">") if map_[(x + 1, y)] != "#" else (x, y, "v")
        else:
            raise RuntimeError
    except KeyError:
        pass
    return next_guard


map_, guard = _get_map()
path: set[Guard] = set()
while guard not in path:
    path.add(guard)
    guard = _move_guard(map_, guard)
print(f"Part 1: {len(set((x, y) for x, y, _ in path))}")


num_obstructions = 0
for map_, guard in _generate_obstructions(set((k, v) for k, v, _ in path)):
    path: set[Guard] = set()
    while guard not in path:
        path.add(guard)
        next_guard = _move_guard(map_, guard)
        if next_guard != guard and next_guard in path:
            num_obstructions += 1
            break
        guard = next_guard
print(f"Part 2: {num_obstructions}")
