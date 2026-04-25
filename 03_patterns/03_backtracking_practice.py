"""
03_backtracking_practice.py  —  TYPE FROM SCRATCH
"""


# ============================================================
# 1. subsets(nums) -> list[list[int]]
# ============================================================

def subsets(nums):
    result = []

    def backtrack(start, path):
        # TODO: append a snapshot path[:] to result
        # TODO: for i in range(start, len(nums)): pick, recurse(i+1), undo
        pass

    backtrack(0, [])
    return result


# ============================================================
# 2. permutations(nums) -> list[list[int]]
# ============================================================

def permutations(nums):
    result = []

    def backtrack(path, used):
        # TODO: if len(path) == len(nums), record path[:] and return
        # TODO: for each unused i, mark used, append, recurse, pop, unmark
        pass

    backtrack([], [False] * len(nums))
    return result


# ============================================================
# 3. combinations(n, k) -> list[list[int]]
# ============================================================

def combinations(n, k):
    result = []

    def backtrack(start, path):
        # TODO: if len(path) == k, record snapshot and return
        # TODO: for i in range(start, n+1): pick, recurse(i+1), undo
        pass

    backtrack(1, [])
    return result


# ============================================================
# 4. exist(board, word) -> bool   (Word Search)
# ============================================================

DIRECTIONS_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, idx):
        # TODO: if idx == len(word): return True
        # TODO: bounds + char match check
        # TODO: mark visited (saved + replace), recurse 4 dirs, restore, return
        pass

    # TODO: try every starting cell
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    s = subsets([1, 2, 3])
    assert sorted(s) == sorted([[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])

    p = permutations([1, 2, 3])
    assert sorted(p) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3],
                                [2, 3, 1], [3, 1, 2], [3, 2, 1]])

    c = combinations(4, 2)
    assert sorted(c) == sorted([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])

    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    assert exist(board, "ABCCED") is True
    assert exist(board, "SEE") is True
    assert exist(board, "ABCB") is False

    print("✅ All tests passed.")
