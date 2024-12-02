import re
import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.read()

    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    result = 0
    for match in re.finditer(regex, data):
        left, right = match.groups()
        result += int(left) * int(right)
    assert result == 173785482
    print(f"Part A: {result}")

    regex = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
    result = 0
    enabled = True
    for match in re.finditer(regex, data):
        left, right, do, dont = match.groups()
        if enabled and left:
            result += int(left) * int(right)
        if do:
            enabled = True
        if dont:
            enabled = False
    assert result == 83158140
    print(f"Part B: {result}")
