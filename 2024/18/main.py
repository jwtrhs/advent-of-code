import itertools
import sys
import typing

Position = tuple[int, int]
Map = dict[Position, str]
Path = list[Position]

bytes_: list[Position] = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        x, y = line.split(",")
        bytes_.append((int(x), int(y)))

SIDE = max(x for x, _ in bytes_) + 1
DEBUG = False

map_: Map = {(x, y): "." for x, y in itertools.product(range(0, SIDE), range(0, SIDE))}


def print_map(map_: dict[Position, str], path: set[Position] | None = None):
    path = path or set()
    width = max(x for x, _ in map_.keys()) + 1
    height = max(y for _, y in map_.keys()) + 1
    line = "\n".join(
        "".join("0" if (x, y) in path else map_[(x, y)] for x in range(0, width))
        for y in range(0, height)
    )
    print(line)
    print()


def solve(
    map_: Map, bytes_: list[Position], start: Position, end: Position, after: int
) -> list[Position] | None:
    fallen_map = {p: "." if p not in bytes_[:after] else "#" for p in map_.keys()}
    if DEBUG:
        print_map(fallen_map)
    paths: list[list[Position]] = [[start]]
    visited: dict[Position, int] = {}
    solution: list[Position] | None = None
    while paths and not solution:
        path = paths.pop(0)
        if DEBUG:
            print_map(fallen_map, set(path))
        x, y = path[-1]
        if (x, y) == end:
            solution = path
            break
        moves: list[Position] = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        ]
        for move in moves:
            if move not in fallen_map or move in path or fallen_map[move] != ".":
                continue
            new_path = path + [move]
            if move in visited and visited[move] <= len(new_path):
                continue
            visited[move] = len(new_path)
            paths.append(new_path)
    return solution


def solve_blocked(map_: Map, bytes_: list[Position]) -> Position | None:
    def _edges(p: Position) -> set[str]:
        edges = set()
        if p[0] == 0:
            edges.add("L")
        if p[0] == SIDE - 1:
            edges.add("R")
        if p[1] == 0:
            edges.add("T")
        if p[1] == SIDE - 1:
            edges.add("B")
        return edges

    def _edges_block(edges: set[str]) -> bool:
        return (
            bool(edges.issuperset(["L", "T"]))
            or bool(edges.issuperset(["L", "R"]))
            or bool(edges.issuperset(["R", "B"]))
            or bool(edges.issuperset(["T", "B"]))
        )

    def _is_next_to(p: Position, s: set[Position]) -> bool:
        x, y = p
        n: set[Position] = set(
            [
                (x - 1, y - 1),
                (x - 1, y),
                (x - 1, y + 1),
                (x, y - 1),
                (x, y + 1),
                (x + 1, y - 1),
                (x + 1, y),
                (x + 1, y + 1),
            ]
        )
        return bool(set.intersection(n, s))

    byte_sets: dict[Position, tuple[set[Position], set[str]]] = {}
    for byte in bytes_:
        sets_to_merge = {k: v for k, v in byte_sets.items() if _is_next_to(byte, v[0])}
        new_set_positions = set([byte])
        new_set_edges = _edges(byte)
        for k, v in sets_to_merge.items():
            new_set_positions |= v[0]
            new_set_edges |= v[1]
            del byte_sets[k]
        byte_sets[byte] = (new_set_positions, new_set_edges)
        if _edges_block(new_set_edges):
            if DEBUG:
                print_map(map_, new_set_positions)
            return byte


solution = solve(map_, bytes_, (0, 0), (70, 70), 1024)
print(f"Part 1: {len(solution) - 1 if solution else None}")

print(f"Part 2: {solve_blocked(map_, bytes_)}")
