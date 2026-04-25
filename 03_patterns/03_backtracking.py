"""
03_backtracking.py  —  REFERENCE FILE

Backtracking template.

Use when:
  - Generate all subsets / permutations / combinations
  - "Find all valid configurations of ___"
  - Word search / N-Queens / Sudoku

Universal template:
    def backtrack(path, choices):
        if base case: record path
        for choice in choices:
            make choice
            backtrack(path + [choice], remaining choices)
            undo choice
"""


# ============================================================
# 1. Subsets — all 2^n subsets
# ============================================================

def subsets(nums: list[int]) -> list[list[int]]:
    """Return all subsets of nums."""
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        result.append(path[:])             # snapshot
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()                     # undo

    backtrack(0, [])
    return result


# ============================================================
# 2. Permutations — all n! orderings
# ============================================================

def permutations(nums: list[int]) -> list[list[int]]:
    """Return all permutations of nums (assumes distinct)."""
    result: list[list[int]] = []

    def backtrack(path: list[int], used: list[bool]) -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


# ============================================================
# 3. Combinations — choose k from n
# ============================================================

def combinations(n: int, k: int) -> list[list[int]]:
    """All combinations of k numbers from 1..n."""
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result


# ============================================================
# 4. Word Search on a 2D grid
# ============================================================

DIRECTIONS_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def exist(board: list[list[str]], word: str) -> bool:
    """True if word can be built by adjacent cells (no reuse)."""
    rows, cols = len(board), len(board[0])

    def backtrack(r: int, c: int, idx: int) -> bool:
        if idx == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[idx]:
            return False

        # mark visited by mutating in place (will restore after)
        saved = board[r][c]
        board[r][c] = "#"

        for dr, dc in DIRECTIONS_4:
            if backtrack(r + dr, c + dc, idx + 1):
                board[r][c] = saved
                return True

        board[r][c] = saved                # restore
        return False

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    # [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]

    print(permutations([1, 2, 3]))
    # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    print(combinations(4, 2))
    # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    print(exist(board, "ABCCED"))   # True
    print(exist(board, "SEE"))      # True
    print(exist(board, "ABCB"))     # False
