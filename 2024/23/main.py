import collections
import itertools
import sys
import typing

Connections = dict[str, set[str]]
Set = set[str]

connections: Connections = collections.defaultdict(set)
with open(sys.argv[1]) as f:
    for line in f.readlines():
        if not line.strip():
            continue
        a, b = line.strip().split("-")
        connections[a].add(b)
        connections[b].add(a)


def triplets() -> set[tuple[str, str, str]]:
    sets = set()
    for pc in connections.keys():
        if not pc.startswith("t"):
            continue
        for pc2, pc3 in itertools.combinations(connections[pc], r=2):
            if pc3 in connections[pc2] and pc2 in connections[pc3]:
                sets.add(tuple(sorted([pc, pc2, pc3])))
    return sets


def bors_kerbosch_v2(
    R: Set, P: Set, X: Set, G: Connections
) -> typing.Generator[list[str], None, None]:
    if len(P) == 0 and len(X) == 0:
        if len(R) > 2:
            yield sorted(R)
        return

    (d, pivot) = max([(len(G[v]), v) for v in P.union(X)])

    for v in P.difference(G[pivot]):
        yield from bors_kerbosch_v2(
            R.union(set([v])), P.intersection(G[v]), X.intersection(G[v]), G
        )
        P.remove(v)
        X.add(v)


print(f"Part 1: {len(triplets())}")

results = list(bors_kerbosch_v2(set([]), set(connections.keys()), set([]), connections))
print(f"Part 2: {",".join(max(results, key=lambda x: len(x)))}")
