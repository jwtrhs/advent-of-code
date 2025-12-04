import sys

batteries = [
    line.strip() for line in open(sys.argv[1], "r").readlines() if line.strip()
]


def _joltage(battery: str, length: int) -> int:
    b = list(enumerate(battery))
    jolts = []
    for i in range(0, length):
        start_index = jolts[-1][0] + 1 if jolts else 0
        jolts.append(max(b[start_index : len(b) - length + i + 1], key=lambda x: x[1]))
    return int("".join(j[1] for j in jolts))


print(f"Part 1: {sum(_joltage(b, 2) for b in batteries)}")
print(f"Part 2: {sum(_joltage(b, 12) for b in batteries)}")
