import functools
import sys
import typing


Position = tuple[int, int]
Path = list[Position]
Map = dict[Position, str]
Move = typing.Literal["^", ">", "<", "v", "A"]

DEBUG = False

CODES = [l.strip() for l in open(sys.argv[1]) if l.strip()]

NUMERIC_KEYPAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [" ", "0", "A"],
]
NUMERIC_KEYPAD_MAP = {
    (x, y): v for y, row in enumerate(NUMERIC_KEYPAD) for x, v in enumerate(row)
}

DIRECTIONAL_KEYPAD = [[" ", "^", "A"], ["<", "v", ">"]]
DIRECTIONAL_KEYPAD_MAP = {
    (x, y): v for y, row in enumerate(DIRECTIONAL_KEYPAD) for x, v in enumerate(row)
}


def is_valid(map_: Map, start: Position, moves: list[str]) -> bool:
    p = start
    for move in moves:
        if move == "<":
            p = (p[0] - 1, p[1])
        if move == ">":
            p = (p[0] + 1, p[1])
        if move == "^":
            p = (p[0], p[1] - 1)
        if move == "v":
            p = (p[0], p[1] + 1)
        if map_[p] == " ":
            return False
    return True


def moves(map_: Map, items: typing.Iterable[str]) -> list[str]:
    a = next(k for k, v in map_.items() if v == "A")
    start = a
    moves_ = []
    for item in items:
        end = next(k for k, v in map_.items() if v == item)
        assert start in map_ and end in map_
        x_dist = end[0] - start[0]
        y_dist = end[1] - start[1]
        left = ["<"] * -x_dist
        right = [">"] * x_dist
        up = ["^"] * -y_dist
        down = ["v"] * y_dist
        if is_valid(map_, start, left + up + down + right):
            next_moves = left + up + down + right + ["A"]
        else:
            next_moves = right + down + up + left + ["A"]
        moves_ += next_moves
        start = end
    return moves_


score = 0
for code in CODES:
    moves_ = moves(NUMERIC_KEYPAD_MAP, code)
    for i in range(0, 2):
        moves_ = moves(DIRECTIONAL_KEYPAD_MAP, moves_)
    score += len(moves_) * int(code[:-1])
print(f"Part 1: {score}")
