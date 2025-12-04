import sys

input_ = [
    tuple(r.strip().split("-"))
    for r in open(sys.argv[1]).readline().split(",")
    if r.strip()
]


def _invalid_ids(input_: list[tuple]) -> list[int]:
    invalid_ids = []
    for start, end in input_:
        for v in range(int(start), int(end) + 1):
            s = str(v)
            if len(s) % 2 != 0:
                continue
            index = int(len(s) / 2)
            if s[:index] == s[index:]:
                invalid_ids.append(v)

    return invalid_ids


def _invalid_ids_2(input_: list[tuple]) -> list[int]:
    invalid_ids = []
    for start, end in input_:
        for v in range(int(start), int(end) + 1):
            s = str(v)
            for slice in range(1, int(len(s) / 2 + 1)):
                if (len(s) / slice) % 1 != 0:
                    continue
                repetitions = [s[i : i + slice] for i in range(0, len(s), slice)]
                if all(r == repetitions[0] for r in repetitions):
                    invalid_ids.append(v)
                    break
    return invalid_ids


print(f"Part 1: {sum(_invalid_ids(input_))}")
print(f"Part 2: {sum(_invalid_ids_2(input_))}")
