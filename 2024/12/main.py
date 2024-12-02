import collections
import sys
from typing import Literal

Point = tuple[int, int]
Plant = str
Region = set[Point]
Side = Literal["Left", "Right", "Up", "Down"]
Fence = tuple[Point, Side]

data = [l.strip() for l in open(sys.argv[1]) if l.strip()]
map_: dict[Point, Plant] = {
    (x, y): plant for y, row in enumerate(data) for x, plant in enumerate(row)
}


visited: set[Point] = set()
regions: dict[Point, Region] = collections.defaultdict(set)
for point, plant in map_.items():
    potential_plants_in_region: list[Point] = [point]
    count = 0
    while potential_plants_in_region:
        count += 1
        next_ = potential_plants_in_region.pop()
        if next_ in visited or next_ not in map_ or map_[next_] != map_[point]:
            continue
        regions[point].add(next_)
        visited.add(next_)
        potential_plants_in_region.extend(
            [
                (next_[0] - 1, next_[1]),
                (next_[0] + 1, next_[1]),
                (next_[0], next_[1] - 1),
                (next_[0], next_[1] + 1),
            ]
        )


fences: dict[Point, set[Fence]] = collections.defaultdict(set)
for point, plant in map_.items():
    left: Point = (point[0] - 1, point[1])
    right: Point = (point[0] + 1, point[1])
    up: Point = (point[0], point[1] - 1)
    down: Point = (point[0], point[1] + 1)

    if map_.get(left) != plant:
        fences[point].add((point, "Left"))
    if map_.get(right) != plant:
        fences[point].add((point, "Right"))
    if map_.get(up) != plant:
        fences[point].add((point, "Up"))
    if map_.get(down) != plant:
        fences[point].add((point, "Down"))


def fences_are_next_to_each_other(fence1: Fence, fence2: Fence) -> bool:
    if fence1 == fence2:
        return True

    if map_[fence1[0]] != map_[fence2[0]]:
        # Fences must be for the same plant
        return False

    if fence1[1] != fence2[1]:
        # Fences must be on the same side
        return False

    if (
        (fence1[1] == "Right" or fence1[1] == "Left")
        and fence1[0][0] == fence2[0][0]
        and (fence1[0][1] == fence2[0][1] - 1 or fence1[0][1] == fence2[0][1] + 1)
    ):
        return True
    if (
        (fence1[1] == "Up" or fence1[1] == "Down")
        and fence1[0][1] == fence2[0][1]
        and (fence1[0][0] == fence2[0][0] - 1 or fence1[0][0] == fence2[0][0] + 1)
    ):
        return True
    return False


visited_: set[Fence] = set()
sides: dict[Fence, set[Fence]] = collections.defaultdict(set)
for point, fences_ in fences.items():
    for fence in fences_:
        potential_fences: list[Fence] = [fence]
        while potential_fences:
            next_fence = potential_fences.pop()
            if next_fence in visited_:
                continue
            if not sides[fence] or any(
                fences_are_next_to_each_other(next_fence, f) for f in sides[fence]
            ):
                sides[fence].add(next_fence)
                visited_.add(next_fence)
                potential_fences.extend(
                    fences.get((next_fence[0][0] - 1, next_fence[0][1]), [])
                )
                potential_fences.extend(
                    fences.get((next_fence[0][0] + 1, next_fence[0][1]), [])
                )
                potential_fences.extend(
                    fences.get((next_fence[0][0], next_fence[0][1] - 1), [])
                )
                potential_fences.extend(
                    fences.get((next_fence[0][0], next_fence[0][1] + 1), [])
                )


sum_ = 0
for _, points in regions.items():
    sum_ += len(points) * sum(len(fences[p]) for p in points)
print(f"Part 1: {sum_}")


sum_ = 0
for _, points in regions.items():
    sum_ += len(points) * sum(
        1 if len(sides[f]) else 0 for p in points for f in fences[p]
    )
print(f"Part 2: {sum_}")
