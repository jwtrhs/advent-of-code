import functools
import itertools
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


def all_moves(map_: Map, items: typing.Iterable[str]) -> list[str]:
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


def moves(map_: Map, start: Position, end: Position) -> list[str]:
    assert start in map_
    assert end in map_
    x_dist = end[0] - start[0]
    y_dist = end[1] - start[1]
    left = ["<"] * -x_dist
    right = [">"] * x_dist
    up = ["^"] * -y_dist
    down = ["v"] * y_dist
    if is_valid(map_, start, left + up + down + right):
        return left + up + down + right + ["A"]
    else:
        return right + down + up + left + ["A"]


@functools.cache
def directional(start: Position, end: Position, r: int) -> int:
    moves_ = moves(DIRECTIONAL_KEYPAD_MAP, start, end)
    if r == 1:
        return len(moves_)
    sum_ = sum(
        directional(
            next(p for p, v in DIRECTIONAL_KEYPAD_MAP.items() if v == a),
            next(p for p, v in DIRECTIONAL_KEYPAD_MAP.items() if v == b),
            r=r - 1,
        )
        for a, b in itertools.pairwise(["A"] + moves_)
    )
    return sum_


def numeric(code: str, r: int) -> int:
    sum_ = 0
    for a, b in itertools.pairwise("A" + code):
        start = next(p for p, v in NUMERIC_KEYPAD_MAP.items() if v == a)
        end = next(p for p, v in NUMERIC_KEYPAD_MAP.items() if v == b)
        moves_ = moves(NUMERIC_KEYPAD_MAP, start, end)
        sum_ += sum(
            directional(
                next(p for p, v in DIRECTIONAL_KEYPAD_MAP.items() if v == a),
                next(p for p, v in DIRECTIONAL_KEYPAD_MAP.items() if v == b),
                r=r,
            )
            for a, b in itertools.pairwise(["A"] + moves_)
        )
    return sum_


score = 0
for code in CODES:
    moves_ = all_moves(NUMERIC_KEYPAD_MAP, code)
    for i in range(0, 2):
        moves_ = all_moves(DIRECTIONAL_KEYPAD_MAP, moves_)
    score += len(moves_) * int(code[:-1])
print(f"Part 1: {score}")

part2 = sum(numeric(code, r=25) * int(code[:-1]) for code in CODES)
print(f"Part 2: {part2}")
