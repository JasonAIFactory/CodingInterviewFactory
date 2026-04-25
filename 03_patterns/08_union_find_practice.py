"""
08_union_find_practice.py  —  TYPE FROM SCRATCH
"""


# ============================================================
# UnionFind class
#   - parent[]
#   - rank[]
#   - components count
#   - find(x): path compression
#   - union(x, y): union by rank, returns True if merged
#   - connected(x, y): bool
# ============================================================

class UnionFind:
    def __init__(self, n):
        # TODO: parent = list(range(n)); rank = [0]*n; components = n
        pass

    def find(self, x):
        # TODO: if parent[x] != x: parent[x] = find(parent[x]) (compression)
        # TODO: return parent[x]
        pass

    def union(self, x, y):
        # TODO: rx, ry = find(x), find(y)
        # TODO: if equal return False
        # TODO: union by rank — attach smaller to larger
        # TODO: bump rank if equal; decrement components; return True
        pass

    def connected(self, x, y):
        # TODO: find(x) == find(y)
        pass


# ============================================================
# num_provinces(is_connected) -> int
# ============================================================

def num_provinces(is_connected):
    # TODO: n = len; build UnionFind(n)
    # TODO: union(i, j) when is_connected[i][j] == 1 (j > i to avoid double work)
    # TODO: return uf.components
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    uf = UnionFind(5)
    assert uf.union(0, 1) is True
    assert uf.union(0, 1) is False        # already merged
    assert uf.connected(0, 1) is True
    assert uf.connected(0, 2) is False
    uf.union(2, 3)
    uf.union(1, 2)
    assert uf.connected(0, 3) is True
    assert uf.components == 2

    assert num_provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert num_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3

    print("✅ All tests passed.")
