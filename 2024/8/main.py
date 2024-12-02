import itertools
import sys

Point = tuple[int, int]
Antenna = tuple[Point, str]
Map = dict[Point, str]

with open(sys.argv[1]) as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

map_: Map = {
    (x, y): lines[y][x] for x in range(0, len(lines[0])) for y in range(0, len(lines))
}
antennas: list[Antenna] = [(k, v) for k, v in map_.items() if v != "."]

antinode_locations: set[Point] = set()
for antenna1, antenna2 in itertools.product(antennas, repeat=2):
    point1, value1 = antenna1
    point2, value2 = antenna2
    if point1 == point2 or value1 != value2:
        continue
    antinode_location: Point = (2 * point1[0] - point2[0], 2 * point1[1] - point2[1])
    if antinode_location not in map_.keys():
        continue
    antinode_locations.add(antinode_location)
print(f"Part 1: {len(antinode_locations)}")

antinode_locations: set[Point] = set()
for antenna1, antenna2 in itertools.product(antennas, repeat=2):
    point1, value1 = antenna1
    point2, value2 = antenna2
    if point1 == point2 or value1 != value2:
        continue
    antinode_location: Point = point1
    point_offset: Point = (point1[0] - point2[0], point1[1] - point2[1])
    while antinode_location in map_.keys():
        antinode_locations.add(antinode_location)
        antinode_location: Point = (
            antinode_location[0] - point_offset[0],
            antinode_location[1] - point_offset[1],
        )
print(f"Part 2: {len(antinode_locations)}")
