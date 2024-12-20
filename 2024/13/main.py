import itertools
import sys


Point = tuple[int, int]
Button = Point
Prize = Point
Game = tuple[Button, Button, Prize]


def parse_line(s: str) -> tuple[int, int]:
    _, offset = s.split(":", 1)
    x, y = offset.split(",")
    return int(x.strip()[2:]), int(y.strip()[2:])


games: list[Game] = []

with open(sys.argv[1]) as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]
    for button_a, button_b, prize in itertools.batched(lines, 3):
        games.append((parse_line(button_a), parse_line(button_b), parse_line(prize)))


def calculate_brute_force(games: list[Game]) -> int:
    sum_ = 0
    for button_a, button_b, prize in games:
        costs: list[int] = []
        for a, b in itertools.product(range(0, 101), repeat=2):
            move_a = (button_a[0] * a, button_a[1] * a)
            move_b = (button_b[0] * b, button_b[1] * b)
            total = (move_a[0] + move_b[0], move_a[1] + move_b[1])
            if total == prize:
                costs.append((a * 3) + b)
        if costs:
            sum_ += min(costs)
    return sum_


def calculate_linalg(games: list[Game]) -> int:
    sum_ = 0
    for button_a, button_b, prize in games:
        a_x, a_y = button_a
        b_x, b_y = button_b
        p_x, p_y = prize

        # see: https://en.wikipedia.org/wiki/Cramer%27s_rule
        na = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
        nb = (a_x * p_y - a_y * p_x) / (a_x * b_y - a_y * b_x)
        if na % 1 == 0 and nb % 1 == 0:
            sum_ += round(na) * 3 + round(nb)

    return sum_


print(f"Part 1: {calculate_brute_force(games)}")
print(f"Part 1: {calculate_linalg(games)}")
part2_games = [
    (a, b, (p[0] + 10000000000000, p[1] + 10000000000000)) for a, b, p in games
]
print(f"Part 2: {calculate_linalg(part2_games)}")
