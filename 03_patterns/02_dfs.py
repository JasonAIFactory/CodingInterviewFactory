"""
02_dfs.py  —  REFERENCE FILE

DFS (Depth-First Search) template.

Use when:
  - All paths / all combinations
  - Connected components
  - Tree traversal (preorder / inorder / postorder)
  - Topological-style problems

Both recursive AND iterative versions — interviewers may ask either.
"""


# ============================================================
# 1. DFS on a graph (recursive)
# ============================================================

def dfs_graph(graph: dict[int, list[int]], start: int) -> list[int]:
    """Return nodes in DFS visit order."""
    visited: set[int] = set()
    order: list[int] = []

    def dfs(node: int) -> None:
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(start)
    return order


# ============================================================
# 2. DFS on a graph (iterative — explicit stack)
# ============================================================

def dfs_graph_iter(graph: dict[int, list[int]], start: int) -> list[int]:
    """Iterative DFS. Useful when recursion depth would overflow."""
    visited: set[int] = set()
    stack: list[int] = [start]
    order: list[int] = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # reverse neighbor order so the leftmost is on top of the stack
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
    return order


# ============================================================
# 3. Count connected components (undirected graph)
# ============================================================

def count_components(n: int, edges: list[list[int]]) -> int:
    """n nodes labeled 0..n-1; edges is undirected list of [u, v]."""
    graph: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited: set[int] = set()

    def dfs(node: int) -> None:
        visited.add(node)
        for nb in graph[node]:
            if nb not in visited:
                dfs(nb)

    components = 0
    for i in range(n):
        if i not in visited:
            components += 1
            dfs(i)
    return components


# ============================================================
# 4. Tree DFS — preorder / inorder / postorder (recursive)
# ============================================================

class TreeNode:
    def __init__(self, val: int, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# ============================================================
# 5. Tree DFS — iterative inorder (classic interview)
# ============================================================

def inorder_iter(root: TreeNode | None) -> list[int]:
    """Iterative inorder using explicit stack."""
    result: list[int] = []
    stack: list[TreeNode] = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    g = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
    print(dfs_graph(g, 1))                            # [1, 2, 4, 3, 5]
    print(dfs_graph_iter(g, 1))                       # [1, 2, 4, 3, 5]
    print(count_components(5, [[0, 1], [1, 2], [3, 4]]))   # 2

    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    print(preorder(root))                             # [1, 2, 4, 3, 5]
    print(inorder(root))                              # [4, 2, 1, 3, 5]
    print(postorder(root))                            # [4, 2, 5, 3, 1]
    print(inorder_iter(root))                         # [4, 2, 1, 3, 5]
