import sys
import typing

with open(sys.argv[1]) as f:
    lines = f.readlines()

score = 0
for line in lines:
    target, values = line.split(":", 1)
    target = int(target)
    values = [int(v.strip()) for v in values.split(" ") if v.strip()]
    result = set([values[0]])
    for v in values[1:]:
        result = set([r + v for r in result] + [r * v for r in result])
    if target in result:
        score += target
print(f"Part 1: {score}")

score = 0
for line in lines:
    target, values = line.split(":", 1)
    target = int(target)
    values = [int(v.strip()) for v in values.split(" ") if v.strip()]
    result = set([values[0]])
    for v in values[1:]:
        result = set(
            [r + v for r in result]
            + [r * v for r in result]
            + [int(str(r) + str(v)) for r in result]
        )
    if target in result:
        score += target
print(f"Part 2: {score}")
