import sys
import typing

Position = tuple[int, int]
Map = dict[Position, str]
Direction = typing.Literal["^", "<", ">", "v"]
Vector = tuple[Position, Direction]
Cost = int
Path = list[tuple[Vector, Cost]]


with open(sys.argv[1]) as f:
    lines = f.readlines()
    map_: Map = {
        (x, y): v
        for y, row in enumerate(lines)
        for x, v in enumerate(row.strip())
        if row.strip()
    }


start = (next(p for p, v in map_.items() if v == "S"), ">")
paths: list[Path] = [[(start, 0)]]
visited: dict[Vector, Cost] = {start: 0}
solutions: list[Path] = []
while paths:
    path = paths.pop(0)
    last_move, last_cost = path[-1]
    p, d = last_move
    if map_[p] == "E":
        if not solutions or solutions[0][-1][1] >= last_cost:
            solutions.append(path)
            solutions = [it for it in solutions if it[-1][1] <= last_cost]
        continue

    offset_x = -1 if d == "<" else 1 if d == ">" else 0
    offset_y = -1 if d == "^" else 1 if d == "v" else 0

    moves: list[Vector] = [
        # Rotation moves
        (p, "<" if d in "^v" else "^"),
        (p, ">" if d in "^v" else "v"),
        # Position moves
        ((p[0] + offset_x, p[1] + offset_y), d),
    ]
    for next_move in moves:
        if map_[next_move[0]] == "#" or next_move[0] in [pos for pos, _ in path]:
            continue
        next_cost = last_cost + (1000 if next_move[1] != last_move[1] else 1)
        next_path = path + [(next_move, next_cost)]
        if next_move not in visited or visited[next_move] >= next_cost:
            visited[next_move] = next_cost
        else:
            continue
        paths.append(next_path)

print(f"Part 1: {min(path[-1][1] for path in solutions)}")
print(f"Part 2: {len(set(it[0][0] for path in solutions for it in path))}")
