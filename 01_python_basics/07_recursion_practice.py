"""
07_recursion_practice.py  —  TYPE FROM SCRATCH
"""

from functools import lru_cache


# ============================================================
# 1. factorial(n) -> int
# factorial(5) -> 120,  factorial(0) -> 1
# ============================================================

def factorial(n):
    # TODO: base case: n <= 1 returns 1
    # TODO: recursive: n * factorial(n - 1)
    pass


# ============================================================
# 2. fib_fast(n) -> int     (use @lru_cache)
# fib_fast(10) -> 55, fib_fast(0) -> 0, fib_fast(1) -> 1
# ============================================================

@lru_cache(maxsize=None)
def fib_fast(n):
    # TODO: base case n < 2 returns n
    # TODO: recursive sum of two previous
    pass


# ============================================================
# 3. climb_stairs(n) -> int     (manual memo with dict)
# climb_stairs(2) -> 2, climb_stairs(3) -> 3, climb_stairs(10) -> 89
# ============================================================

def climb_stairs(n):
    memo = {}

    def dp(i):
        # TODO: base case i <= 1 returns 1
        # TODO: cache check
        # TODO: dp(i - 1) + dp(i - 2)
        pass

    return dp(n)


# ============================================================
# 4. TreeNode + max_depth(node)
# Tree:
#       1
#      / \
#     2   3
#    /
#   4
# max_depth(root) -> 3
# ============================================================

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(node):
    # TODO: base case None returns 0
    # TODO: 1 + max(left depth, right depth)
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert fib_fast(10) == 55
    assert fib_fast(0) == 0
    assert climb_stairs(2) == 2
    assert climb_stairs(10) == 89

    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert max_depth(root) == 3
    print("✅ All tests passed.")
