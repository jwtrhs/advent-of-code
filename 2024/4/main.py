import sys


def _has_xmas(
    data: list[list[str]],
    points: list[tuple[int]],
):
    if any(x >= len(data[0]) or x < 0 or y >= len(data) or y < 0 for x, y in points):
        return 0

    return (
        1
        if (
            data[points[0][1]][points[0][0]] == "X"
            and data[points[1][1]][points[1][0]] == "M"
            and data[points[2][1]][points[2][0]] == "A"
            and data[points[3][1]][points[3][0]] == "S"
        )
        else 0
    )


def has_xmas(data: list[list[str]], x: int, y: int) -> bool:
    if data[y][x] != "X":
        return 0

    horizontal = _has_xmas(
        data,
        [
            (x, y),
            (x + 1, y),
            (x + 2, y),
            (x + 3, y),
        ],
    )

    horizontal_reverse = _has_xmas(
        data,
        [
            (x, y),
            (x - 1, y),
            (x - 2, y),
            (x - 3, y),
        ],
    )

    vertical = _has_xmas(
        data,
        [
            (x, y),
            (x, y + 1),
            (x, y + 2),
            (x, y + 3),
        ],
    )

    vertical_reverse = _has_xmas(
        data,
        [
            (x, y),
            (x, y - 1),
            (x, y - 2),
            (x, y - 3),
        ],
    )

    diagonal_up_left = _has_xmas(
        data,
        [
            (x, y),
            (x - 1, y - 1),
            (x - 2, y - 2),
            (x - 3, y - 3),
        ],
    )

    diagonal_up_right = _has_xmas(
        data,
        [
            (x, y),
            (x + 1, y - 1),
            (x + 2, y - 2),
            (x + 3, y - 3),
        ],
    )

    diagonal_down_left = _has_xmas(
        data,
        [
            (x, y),
            (x - 1, y + 1),
            (x - 2, y + 2),
            (x - 3, y + 3),
        ],
    )

    diagonal_down_right = _has_xmas(
        data,
        [
            (x, y),
            (x + 1, y + 1),
            (x + 2, y + 2),
            (x + 3, y + 3),
        ],
    )

    return (
        horizontal
        + horizontal_reverse
        + vertical
        + vertical_reverse
        + diagonal_up_left
        + diagonal_up_right
        + diagonal_down_left
        + diagonal_down_right
    )


def has_mas(data: list[list[int]], x: int, y: int):
    if data[y][x] != "A":
        return 0

    if x < 1 or x > len(data[0]) - 2:
        return 0
    if y < 1 or y > len(data) - 2:
        return 0

    if not (
        (data[y - 1][x - 1] == "M" and data[y + 1][x + 1] == "S")
        or (data[y - 1][x - 1] == "S" and data[y + 1][x + 1] == "M")
    ):
        return 0

    if not (
        (data[y - 1][x + 1] == "M" and data[y + 1][x - 1] == "S")
        or (data[y - 1][x + 1] == "S" and data[y + 1][x - 1] == "M")
    ):
        return 0

    return 1


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    data = [list(line) for line in lines]

    result = 0
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            result += has_xmas(data, x, y)
    assert result == 2507
    print(f"Part A: {result}")

    result = 0
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            result += has_mas(data, x, y)
    assert result == 1969
    print(f"Part B: {result}")
