"""
07_recursion.py  —  REFERENCE FILE

Goal: Write recursion that does not blow up the stack and is easy to read.

Template — every recursive function has TWO parts:
    1. Base case   — when do I stop?
    2. Recursive case — break the problem into a smaller version of itself.

Memoization = caching results so we don't redo work.
"""

from functools import lru_cache


# ============================================================
# 1. Factorial  —  the simplest recursion
# ============================================================

def factorial(n):
    # SAY: "Base case: 0! is 1.
    #       Recursive case: n! = n * (n-1)!."
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# ============================================================
# 2. Fibonacci  —  shows why memoization matters
# ============================================================

def fib_slow(n):
    """
    O(2^n) without memoization.
    fib_slow(40) is already painful.

    SAY: "This recomputes the same subproblems many times."
    """
    if n < 2:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)


@lru_cache(maxsize=None)
def fib_fast(n):
    """
    O(n) with memoization via @lru_cache.

    SAY: "lru_cache stores results so each n is computed only once.
          This is top-down dynamic programming."
    """
    if n < 2:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)


# ============================================================
# 3. Manual memoization with a dict (interview-friendly)
# ============================================================

def climb_stairs(n):
    """
    Number of distinct ways to climb n stairs (1 or 2 steps at a time).

    SAY: "I memoize using a dict so each subproblem is solved once.
          Total time is O(n)."
    """
    memo = {}

    def dp(i):
        if i <= 1:
            return 1
        if i in memo:
            return memo[i]
        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]

    return dp(n)


# ============================================================
# 4. Recursion on a tree  —  very common in interviews
# ============================================================

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(node):
    """
    SAY: "Base case: empty node has depth 0.
          Recursive case: depth is 1 + max of left and right subtree depths."
    """
    if node is None:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    print(factorial(5))          # 120
    print(fib_fast(30))          # 832040
    print(climb_stairs(10))      # 89

    #     1
    #    / \
    #   2   3
    #  /
    # 4
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    print(max_depth(root))       # 3
