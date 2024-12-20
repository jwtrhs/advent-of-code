import sys

Position = tuple[int, int]
Velocity = tuple[int, int]
Robot = tuple[Position, Velocity]

WIDTH = 101
HEIGHT = 103
robots: list[Robot] = []
with open(sys.argv[1]) as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]
    for line in lines:
        position, velocity = line.split(" ")
        p_x, p_y = position[2:].split(",")
        v_x, v_y = velocity[2:].split(",")
        robots.append(((int(p_x), int(p_y)), (int(v_x), int(v_y))))


def get_positions(robots: list[Robot], t: int) -> list[Position]:
    positions: list[Position] = []
    for position, velocity in robots:
        positions.append(
            (
                (position[0] + velocity[0] * t) % WIDTH,
                (position[1] + velocity[1] * t) % HEIGHT,
            )
        )
    return positions


def get_quadrants(positions: list[Position]):
    q1 = [p for p in positions if p[0] < WIDTH // 2 and p[1] < HEIGHT // 2]
    q2 = [p for p in positions if p[0] > WIDTH // 2 and p[1] < HEIGHT // 2]
    q3 = [p for p in positions if p[0] > WIDTH // 2 and p[1] > HEIGHT // 2]
    q4 = [p for p in positions if p[0] < WIDTH // 2 and p[1] > HEIGHT // 2]
    return q1, q2, q3, q4


def print_tiles(positions: list[Position]):
    for y in range(0, HEIGHT):
        line = (
            str(len([it for it in positions if it == (x, y)]) or ".")
            for x in range(0, WIDTH)
        )
        print("".join(line))
    print()


q1, q2, q3, q4 = get_quadrants(get_positions(robots, t=100))
print(f"Part 1: {len(q1) * len(q2) * len(q3) * len(q4)}")

for t in range(0, 100000):
    positions = get_positions(robots, t=t)
    overlaps = len(positions) / len(set(positions))
    q1, q2, q3, q4 = get_quadrants(positions)
    s1, s2, s3, s4 = len(q1), len(q2), len(q3), len(q4)

    if any(it > 250 for it in (s1, s2, s3, s4)):
        print(f"T={t}")
        print(s1, s2, s3, s4)
        print_tiles(positions)
