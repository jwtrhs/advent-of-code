import itertools
import sys

FREE_SPACE = -1

def _read_disk_map():
    with open(sys.argv[1]) as f:
        return f.readlines()[0].strip()


disk_map = _read_disk_map()
blocks: list[int] = []
for id_, index in enumerate(range(0, len(disk_map), 2)):
    blocks += [id_] * int(disk_map[index])
    blocks += (
        ([FREE_SPACE] * int(disk_map[index + 1])) if index + 1 < len(disk_map) else []
    )


defrag1 = blocks[:]
start = 0
end = len(defrag1) - 1
while True:
    if start > end:
        break
    if defrag1[start] != FREE_SPACE:
        start += 1
        continue
    if defrag1[end] == FREE_SPACE:
        end -= 1
        continue
    defrag1[start] = defrag1[end]
    defrag1[end] = FREE_SPACE
    start += 1
    end -= 1
checksum = sum(index * value for index, value in enumerate(defrag1) if value != -1)
print(f"Part 1: {checksum}")
assert checksum == 6225730762521


def _generate_window(blocks: list[int], reverse: bool = False) -> tuple[int, int, int]:
    if not reverse:
        start = 0
        while start < len(blocks):
            end = start
            while end < len(blocks) and blocks[end] == blocks[start]:
                end += 1
            yield blocks[start], start, end
            start = end
    else:
        end = len(blocks) - 1
        while end > 0:
            start = end
            while start >= -1 and blocks[start] == blocks[end]:
                start -= 1
            yield blocks[start + 1], start + 1, end + 1
            end = start


defrag2: list[Block] = blocks[:]
for from_id, from_start, from_end in _generate_window(blocks, reverse=True):
    if from_id == FREE_SPACE:
        continue
    for to_id, to_start, to_end in _generate_window(defrag2):
        if to_start >= from_start:
            break
        if to_id != FREE_SPACE:
            continue
        if (to_end - to_start) < (from_end - from_start):
            continue
        defrag2[to_start : to_start + (from_end - from_start)] = blocks[
            from_start:from_end
        ]
        defrag2[from_start:from_end] = [FREE_SPACE] * (from_end - from_start)
        break
checksum = sum(index * value for index, value in enumerate(defrag2) if value != -1)
print(f"Part 2: {checksum}")
assert checksum == 6250605700557
