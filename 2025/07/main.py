import sys

diagram = [it.strip() for it in open(sys.argv[1]).readlines() if it.strip()]
map_: dict[tuple[int, int], str] = {
    (x, y): diagram[y][x]
    for y in range(0, len(diagram))
    for x in range(0, len(diagram[y]))
}
columns = max(it[0] for it in map_.keys())
rows = max(it[1] for it in map_.keys())
splits = 0
for y in range(1, rows):
    for x in range(0, columns):
        if map_[(x, y - 1)] in ["S", "|"] and map_[(x, y)] == ".":
            map_[(x, y)] = "|"
    for x in range(0, columns):
        if map_[(x, y - 1)] in ["S", "|"] and map_[(x, y)] == "^":
            if map_.get((x - 1, y)) == ".":
                map_[(x - 1, y)] = "|"
            if map_.get((x + 1, y)) == ".":
                map_[(x + 1, y)] = "|"
            splits += 1
print(f"Part 1: {splits}")
