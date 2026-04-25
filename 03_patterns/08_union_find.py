"""
08_union_find.py  —  REFERENCE FILE

Union-Find (Disjoint Set Union) template.

Use when:
  - Connected components
  - Dynamic merging of groups
  - Cycle detection in undirected graph
  - "Number of provinces / accounts merge / friend circles"

Operations:
  - find(x)        — return the root of x's set, with path compression
  - union(x, y)    — merge sets containing x and y, with union by rank
Both are amortized O(α(n)) — effectively O(1).
"""


class UnionFind:
    def __init__(self, n: int):
        # SAY: "Each element starts as its own parent."
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [0] * n
        self.components: int = n             # number of disjoint sets

    def find(self, x: int) -> int:
        # SAY: "Walk to the root, then flatten the path."
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])    # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Returns True if a merge happened, False if already connected."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        # SAY: "Attach the smaller tree under the larger one."
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# ============================================================
# Application — Number of Provinces (LeetCode 547)
# ============================================================

def num_provinces(is_connected: list[list[int]]) -> int:
    n = len(is_connected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                uf.union(i, j)
    return uf.components


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    print(uf.connected(0, 1))      # True
    print(uf.connected(0, 2))      # False
    uf.union(1, 2)
    print(uf.connected(0, 3))      # True (0-1-2-3 chain)
    print(uf.components)           # 2  (group {0,1,2,3} and {4})

    print(num_provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))   # 2
    print(num_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))   # 3
