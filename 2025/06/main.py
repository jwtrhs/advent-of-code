import functools
import sys

input_ = [
    line.strip().split() for line in open(sys.argv[1], "r").readlines() if line.strip()
]
answers = []
for i in range(0, len(input_[0])):
    values = [int(it[i]) for it in input_[:-1]]
    operation = input_[-1][i]
    if operation == "+":
        answers.append(functools.reduce(lambda a, b: a + b, values))
    else:
        answers.append(functools.reduce(lambda a, b: a * b, values))
print(f"Part 1: {sum(answers)}")

input_ = [line for line in open(sys.argv[1], "r").readlines() if line.strip()]
answers = []
c = 0
while c < max(len(it) for it in input_):
    operation = input_[-1][c]
    values: list[int] = []
    while True:
        s = functools.reduce(
            lambda a, b: a + b, [it[c] for it in input_[:-1] if c < len(it)]
        ).strip()
        print(s)
        if not s:
            break
        values.append(int(s))
        c += 1
    if operation == "+":
        answers.append(functools.reduce(lambda a, b: a + b, values))
    else:
        answers.append(functools.reduce(lambda a, b: a * b, values))
    c += 1
print(f"Part 2: {sum(answers)}")
