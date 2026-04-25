"""
01_bfs_practice.py  —  TYPE FROM SCRATCH
"""

from collections import deque


# ============================================================
# 1. bfs_graph(graph, start) -> list[int]   (visit order)
# ============================================================

def bfs_graph(graph, start):
    # TODO: visited = {start}
    # TODO: queue = deque([start])
    # TODO: order = []
    # TODO: while queue: pop, append to order, enqueue unvisited neighbors
    pass


# ============================================================
# 2. shortest_path_length(graph, start, target) -> int  (-1 if no path)
# ============================================================

def shortest_path_length(graph, start, target):
    # TODO: if start == target return 0
    # TODO: visited = {start}; queue = deque([(start, 0)])
    # TODO: pop (node, dist). For each neighbor: if target return dist+1; else enqueue (neighbor, dist+1)
    pass


# ============================================================
# 3. shortest_path_grid(grid, start, target) -> int
# 0 = open, 1 = wall, 4-directional
# ============================================================

DIRECTIONS_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def shortest_path_grid(grid, start, target):
    # TODO: rows, cols
    # TODO: handle start/target on a wall
    # TODO: BFS with (r, c, dist), check bounds + grid value + visited
    pass


# ============================================================
# 4. TreeNode + level_order(root) -> list[list[int]]
# ============================================================

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    # TODO: empty root -> []
    # TODO: queue + while loop with level_size = len(queue)
    # TODO: collect a level at a time
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    g = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
    assert bfs_graph(g, 1) == [1, 2, 3, 4, 5]
    assert shortest_path_length(g, 1, 5) == 2
    assert shortest_path_length(g, 1, 1) == 0

    grid = [[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0]]
    assert shortest_path_grid(grid, (0, 0), (2, 3)) == 5

    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    assert level_order(root) == [[1], [2, 3], [4, 5]]
    assert level_order(None) == []

    print("✅ All tests passed.")
