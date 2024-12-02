import sys
import typing

Position = tuple[int, int]
Warehouse = dict[Position, str]
Direction = typing.Literal["^", "<", ">", "v"]


def double(line: str):
    return "".join(
        "##" if v == "#" else "[]" if v == "O" else ".." if v == "." else "@."
        for v in line
    )


def read_input(double_width: bool = False):
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f.readlines()]
    break_ = lines.index("")
    warehouse: Warehouse = {
        (x, y): v
        for y, row in enumerate(lines[:break_])
        for x, v in enumerate(double(row) if double_width else row)
    }
    moves: list[Direction] = typing.cast(
        list[Direction], list("".join(lines[break_ + 1 :]).strip())
    )
    return warehouse, moves


def print_warehouse(warehouse: Warehouse):
    width = max(x for x, _ in warehouse.keys()) + 1
    height = max(y for _, y in warehouse.keys()) + 1
    for y in range(0, height):
        line = "".join(warehouse[(x, y)] for x in range(0, width))
        print(line)


def move_robot(
    warehouse: Warehouse, move: Direction, robot: Position | None = None
) -> Warehouse:
    if not robot:
        robot = next(p for p, v in warehouse.items() if v == "@")
    assert robot and warehouse[robot] == "@"
    assert move in "^<>v"
    offset_x = -1 if move == "<" else 1 if move == ">" else 0
    offset_y = -1 if move == "^" else 1 if move == "v" else 0
    can_move = True
    positions_to_move: list[Position] = []
    positions_to_check: list[Position] = [robot]
    while positions_to_check:
        p = positions_to_check.pop(0)
        if warehouse[p] in "@O":
            positions_to_move.append(p)
            positions_to_check.append((p[0] + offset_x, p[1] + offset_y))
        elif warehouse[p] in "[]":
            p2 = (p[0] + 1, p[1]) if warehouse[p] == "[" else (p[0] - 1, p[1])
            assert warehouse[p2] in "[]"
            if move in "<>":
                positions_to_move.append(p)
                positions_to_move.append(p2)
                positions_to_check.append((p2[0] + offset_x, p2[1] + offset_y))
            else:
                positions_to_move.append(p)
                positions_to_move.append(p2)
                positions_to_check.append((p[0] + offset_x, p[1] + offset_y))
                positions_to_check.append((p2[0] + offset_x, p2[1] + offset_y))
        elif warehouse[p] == "#":
            can_move = False
            break

    # Move robot and boxes
    warehouse = warehouse.copy()
    if can_move:
        for position in reversed(positions_to_move):
            if warehouse[position] == ".":
                continue
            warehouse[(position[0] + offset_x, position[1] + offset_y)] = warehouse[
                position
            ]
            warehouse[position] = "."

    return warehouse


part1, moves = read_input()
for move in moves:
    part1 = move_robot(part1, move)
score = sum(x + 100 * y for (x, y), v in part1.items() if v == "O")
print(f"Part 1: {score}")

part2, moves = read_input(double_width=True)
print_warehouse(part2)
for index, move in enumerate(moves):
    part2 = move_robot(part2, move)
    # print(f"T={index}: {move}")
    # print_warehouse(part2)
score = sum(x + 100 * y for (x, y), v in part2.items() if v == "[")
print(f"Part 2: {score}")
