import re
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

result = 0
for line in lines:
    matches = list(re.finditer(r"(\d)", line))
    first_num = matches[0].groups()[0]
    last_num = matches[-1].groups()[0]
    result += int(first_num + last_num)
print(f"Part 1: {result}")


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
result = 0
for line in lines:
    for key, value in numbers.items():
        line = line.replace(key, f"{key}{value}{key}")
    matches = list(re.finditer(r"(\d)", line))
    first_num = matches[0].groups()[0]
    last_num = matches[-1].groups()[0]
    result += int(first_num + last_num)
print(f"Part 2: {result}")
