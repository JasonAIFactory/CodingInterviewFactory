"""
03_bfs_dfs.py — Daily drill (type from zero, no peeking)

Target: under 15 minutes.
Patterns: BFS with deque + visited, DFS recursive, grid traversal.
"""

from collections import deque


# === Drill 1: BFS shortest path on graph ===
# Return number of edges in shortest path from start to target.
# Return -1 if unreachable.
# graph: dict[node] = list of neighbors
def bfs_shortest_path(graph: dict[int, list[int]], start: int, target: int) -> int:
    pass


# === Drill 2: DFS — count connected components ===
# n nodes labeled 0..n-1. edges is undirected list of [u, v].
# Return number of connected components.
def count_components(n: int, edges: list[list[int]]) -> int:
    pass


# === Drill 3: Number of Islands ===
# Grid of '1' (land) and '0' (water). Count connected groups (4-directional).
# You CAN mutate the grid.
def num_islands(grid: list[list[str]]) -> int:
    pass


# === Drill 4: Max Depth of Binary Tree ===
class TreeNode:
    def __init__(self, val: int, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    pass


# === Tests ===
if __name__ == "__main__":
    # BFS shortest path
    g = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
    assert bfs_shortest_path(g, 1, 5) == 2
    assert bfs_shortest_path(g, 1, 1) == 0
    assert bfs_shortest_path({1: [], 2: []}, 1, 2) == -1

    # Connected components
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert count_components(5, []) == 5
    assert count_components(3, [[0, 1], [1, 2]]) == 1

    # Number of Islands
    g1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands(g1) == 3

    g2 = [["1", "0"], ["0", "1"]]
    assert num_islands(g2) == 2
    assert num_islands([["0"]]) == 0

    # Max Depth
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert max_depth(root) == 3
    assert max_depth(None) == 0
    assert max_depth(TreeNode(1)) == 1

    print("✅ All BFS/DFS drills passed.")
