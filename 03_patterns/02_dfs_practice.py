"""
02_dfs_practice.py  —  TYPE FROM SCRATCH
"""


# ============================================================
# 1. dfs_graph(graph, start) -> list[int]  (recursive)
# ============================================================

def dfs_graph(graph, start):
    visited = set()
    order = []

    def dfs(node):
        # TODO: skip if visited
        # TODO: mark, append, recurse on neighbors
        pass

    dfs(start)
    return order


# ============================================================
# 2. dfs_graph_iter(graph, start) -> list[int]  (iterative)
# ============================================================

def dfs_graph_iter(graph, start):
    # TODO: stack = [start]; visited = set(); order = []
    # TODO: while stack: pop, skip if visited, mark + append
    # TODO: push neighbors in REVERSED order (so leftmost ends up on top)
    pass


# ============================================================
# 3. count_components(n, edges) -> int   (undirected)
# ============================================================

def count_components(n, edges):
    # TODO: build adjacency list (both directions)
    # TODO: DFS from every unvisited node, count starts
    pass


# ============================================================
# 4. TreeNode + preorder / inorder / postorder
# ============================================================

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    # TODO: [root.val] + preorder(left) + preorder(right) ; [] if None
    pass


def inorder(root):
    # TODO: inorder(left) + [root.val] + inorder(right) ; [] if None
    pass


def postorder(root):
    # TODO: postorder(left) + postorder(right) + [root.val] ; [] if None
    pass


# ============================================================
# 5. inorder_iter(root) -> list[int]   (iterative inorder)
# ============================================================

def inorder_iter(root):
    # TODO: stack = []; node = root; result = []
    # TODO: while node or stack: walk left pushing, then pop+visit, then go right
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    g = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
    assert dfs_graph(g, 1) == [1, 2, 4, 3, 5]
    assert dfs_graph_iter(g, 1) == [1, 2, 4, 3, 5]
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2

    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    assert preorder(root) == [1, 2, 4, 3, 5]
    assert inorder(root) == [4, 2, 1, 3, 5]
    assert postorder(root) == [4, 2, 5, 3, 1]
    assert inorder_iter(root) == [4, 2, 1, 3, 5]

    print("✅ All tests passed.")
