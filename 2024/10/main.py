import sys

Height = int
Point = tuple[int, int]
Map = dict[tuple[int, int], int]

data = [l.strip() for l in open(sys.argv[1]) if l.strip()]
map_: Map = {
    (x, y): int(value) for y, row in enumerate(data) for x, value in enumerate(row)
}


def score(map_: Map, point: Point, height: Height) -> list[Point]:
    if point not in map_:
        return []
    if map_[point] != height:
        return []
    if height == 9:
        return [point]
    return (
        score(map_, (point[0] - 1, point[1]), height + 1)
        + score(map_, (point[0] + 1, point[1]), height + 1)
        + score(map_, (point[0], point[1] - 1), height + 1)
        + score(map_, (point[0], point[1] + 1), height + 1)
    )


scores = [score(map_, point, height) for point, height in map_.items() if height == 0]
part1_total = sum(len(set(it)) for it in scores)
print(f"Part 1: {part1_total}")
part2_total = sum(len(it) for it in scores)
print(f"Part 2: {part2_total}")
