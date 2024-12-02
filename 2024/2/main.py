import sys

def read_input(path: str) -> list[list[int]]:
    with open(path) as f:
        lines = f.readlines()
    levels = [it.strip().split(" ") for it in lines]
    return [
        [int(it2) for it2 in it1]
        for it1 in levels
    ]

def permutations(levels: list[int]):
    for i in range(0, len(levels)):
        yield [x for index, x in enumerate(levels) if index != i]

def increasing(levels: list[int]):
    for i in range(0, len(levels) - 1):
        if levels[i] >= levels[i + 1]:
            return False
    return True

def decreasing(levels: list[int]):
    for i in range(0, len(levels) - 1):
        if levels[i] <= levels[i + 1]:
            return False
    return True

def difference(levels: list[int]):
    for i in range(0, len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True

if __name__ == "__main__":
    data = read_input(sys.argv[1])
    
    num_safe = 0
    for levels in data:
        if (increasing(levels) or decreasing(levels)) and difference(levels):
            num_safe += 1
    print(f"Part A: {num_safe}")


    num_safe = 0
    for levels in data:
        for permutation in permutations(levels):
            if (increasing(permutation) or decreasing(permutation)) and difference(permutation):
                num_safe += 1
                break
    print(f"Part B: {num_safe}")
