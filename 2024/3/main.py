import re
import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.read()

    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    result = 0
    for match in re.finditer(regex, data):
        groups = match.groups()
        result += int(groups[0]) * int(groups[1])
    assert result == 173785482
    print(f"Part A: {result}")

    regex = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
    result = 0
    enabled = True
    for match in re.finditer(regex, data):
        groups = match.groups()
        if enabled and groups[0]:
            result += int(groups[0]) * int(groups[1])
        if groups[2]:
            enabled = True
        if groups[3]:
            enabled = False
    assert result == 83158140
    print(f"Part B: {result}")

