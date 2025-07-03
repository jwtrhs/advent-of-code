import itertools
import sys

if __name__ == "__main__":
    locks = []
    keys = []
    with open(sys.argv[1], "r") as f:
        locks_and_keys = [
            list(it)
            for it in itertools.batched(
                [l.strip() for l in f.readlines() if l.strip()], n=7
            )
        ]
    locks = [it for it in locks_and_keys if it[0][0] == "#"]
    keys = [it for it in locks_and_keys if it[0][0] == "."]

    def _columns(lk):
        return [
            sum(1 if lk[y][x] == "#" else 0 for y in range(len(lk))) - 1
            for x in range(len(lk[0]))
        ]

    count_fit = 0
    count_overlap = 0
    for lock, key in itertools.product(locks, keys):
        lock_columns = _columns(lock)
        key_columns = _columns(key)
        overlap = [a + b for a, b in zip(lock_columns, key_columns)]
        if any(it > 5 for it in overlap):
            count_overlap += 1
        else:
            count_fit += 1

    print(count_fit)
