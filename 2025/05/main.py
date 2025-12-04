import sys

grid = {
    (x, y): c
    for y, line in enumerate(open(sys.argv[1], "r").readlines())
    for x, c in enumerate(line)
    if line.strip()
}


def _remove(grid: dict[tuple[int, int], str]) -> dict[tuple[int, int], str]:
    new_grid: dict[tuple[int, int], str] = {}
    for (x, y), c in grid.items():
        if c != "@":
            new_grid[(x, y)] = c
            continue
        neighbours: list[tuple[int, int]] = [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]
        num_adjacent = sum(
            1 if grid.get((x_, y_)) == "@" else 0 for x_, y_ in neighbours
        )
        if num_adjacent < 4:
            new_grid[(x, y)] = "x"
        else:
            new_grid[(x, y)] = "@"

    return new_grid


def _remove_loop(grid: dict[tuple[int, int], str]):
    grids = [grid]
    next_grid = None
    while True:
        next_grid = _remove(grids[-1])
        if next_grid == grids[-1]:
            break
        else:
            grids.append(next_grid)
    return grids[-1]


def _count_removed(grid: dict[tuple[int, int], str]) -> int:
    return sum(c == "x" for c in grid.values())


print(f"Part 1: {_count_removed(_remove(grid))}")
print(f"Part 2: {_count_removed(_remove_loop(grid))}")
