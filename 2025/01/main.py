import sys

input_ = [(l[0], int(l[1:])) for l in open(sys.argv[1], "r").readlines() if l.strip()]


def _count_zeros(input_: list[tuple[str, int]]) -> int:
    count = 0
    position = 50  # start position
    for direction, distance in input_:
        if direction == "L":
            distance = -distance
        position = (position + distance) % 100
        if position == 0:
            count += 1
    return count


def _count_zeros_clicks(input_: list[tuple[str, int]]) -> int:
    count = 0
    position = 50
    for direction, distance in input_:
        for _ in range(0, abs(distance)):
            if direction == "R":
                position += 1
            else:
                position -= 1
            position = position % 100
            if position == 0:
                count += 1
    return count


print(f"Part 1: {_count_zeros(input_)}")
print(f"Part 2: {_count_zeros_clicks(input_)}")
