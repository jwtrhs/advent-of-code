import itertools
import math
import sys

Box = tuple[int, int, int]
Circuit = frozenset[Box]


def _get_input() -> list[Box]:
    input_ = [
        line.strip().split(",")
        for line in open(sys.argv[1], "r").readlines()
        if line.strip()
    ]
    return [(int(it[0]), int(it[1]), int(it[2])) for it in input_]


def _distance(box1: Box, box2: Box) -> float:
    return math.sqrt(
        pow(box1[0] - box2[0], 2)
        + pow(box1[1] - box2[1], 2)
        + pow(box1[2] - box2[2], 2)
    )


def _distances(boxes: list[Box]) -> list[tuple[tuple[Box, Box], float]]:
    distances: list[tuple[tuple[Box, Box], float]] = []
    for box1, box2 in itertools.combinations(boxes, 2):
        distances.append(((box1, box2), _distance(box1, box2)))
    return sorted(distances, key=lambda x: x[1])


def _overlap(circuit1: Circuit, circuit2: Circuit) -> bool:
    return bool(circuit1.intersection(circuit2))


def _merge(circuits: set[Circuit]) -> set[Circuit]:
    new_circuits = circuits
    next_circuits = circuits
    while True:
        for a, b in itertools.combinations(new_circuits, 2):
            if _overlap(a, b):
                next_circuits = new_circuits.difference([a, b]).union([a.union(b)])
                break
        if next_circuits == new_circuits:
            break
        new_circuits = next_circuits
    return new_circuits


def part1() -> int:
    boxes = _get_input()
    distances = _distances(boxes)

    circuits: set[Circuit] = set()
    for i in range(0, int(sys.argv[2])):
        box1, box2 = distances[i][0]
        circuits.add(frozenset([box1, box2]))
        circuits = _merge(circuits)
    lengths = sorted(len(it) for it in circuits)
    return lengths[-3] * lengths[-2] * lengths[-1]


def part2() -> int:
    boxes = _get_input()
    distances = _distances(boxes)
    circuits: set[Circuit] = set()
    last_joined_score = 0
    for (box1, box2), _ in distances:
        circuits.add(frozenset([box1, box2]))
        circuits = _merge(circuits)
        last_joined_score = box1[0] * box2[0]
        if len(circuits) == 1 and len(circuits.copy().pop()) == len(boxes):
            break
    return last_joined_score


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
