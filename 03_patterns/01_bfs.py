"""
01_bfs.py  —  REFERENCE FILE

BFS (Breadth-First Search) template.

Use when:
  - Shortest path in unweighted graph / grid
  - Level-order tree traversal
  - "Smallest number of steps to ___"

Always need:
  - deque as FIFO queue
  - visited set to avoid revisits
"""

from collections import deque


# ============================================================
# 1. BFS on a graph (adjacency list)
# ============================================================

def bfs_graph(graph: dict[int, list[int]], start: int) -> list[int]:
    """Return nodes in BFS visit order."""
    visited: set[int] = {start}
    queue: deque[int] = deque([start])
    order: list[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


# ============================================================
# 2. BFS shortest path length (unweighted)
# ============================================================

def shortest_path_length(graph: dict[int, list[int]], start: int, target: int) -> int:
    """Return number of edges in shortest path; -1 if unreachable."""
    if start == target:
        return 0

    visited: set[int] = {start}
    queue: deque[tuple[int, int]] = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == target:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1


# ============================================================
# 3. BFS on a 2D grid (4-directional)
# ============================================================

DIRECTIONS_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def shortest_path_grid(grid: list[list[int]],
                       start: tuple[int, int],
                       target: tuple[int, int]) -> int:
    """Return shortest steps in grid where 0 = open, 1 = wall."""
    rows, cols = len(grid), len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[target[0]][target[1]] == 1:
        return -1

    visited: set[tuple[int, int]] = {start}
    queue: deque[tuple[int, int, int]] = deque([(*start, 0)])

    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == target:
            return dist
        for dr, dc in DIRECTIONS_4:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 0
                    and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1


# ============================================================
# 4. BFS on a tree — level order
# ============================================================

class TreeNode:
    def __init__(self, val: int, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return values grouped by level."""
    if root is None:
        return []
    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        level: list[int] = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    g = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
    print(bfs_graph(g, 1))                              # [1, 2, 3, 4, 5]
    print(shortest_path_length(g, 1, 5))                # 2

    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
    ]
    print(shortest_path_grid(grid, (0, 0), (2, 3)))     # 5

    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    print(level_order(root))                            # [[1], [2, 3], [4, 5]]
