"""
07_backtracking.py — Daily drill (type from zero, no peeking)

Target: under 10 minutes.
Patterns: pick / recurse / undo. Snapshot path[:] when recording.
"""


# === Drill 1: Subsets ===
# Return all 2^n subsets of nums (assume distinct).
def subsets(nums: list[int]) -> list[list[int]]:
    pass


# === Drill 2: Permutations ===
# Return all n! orderings of nums (assume distinct).
def permutations(nums: list[int]) -> list[list[int]]:
    pass


# === Drill 3: Combination Sum ===
# Return all unique combinations from candidates that sum to target.
# Each candidate may be used UNLIMITED times.
# Candidates are distinct positive integers.
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    pass


# === Tests ===
if __name__ == "__main__":
    # Subsets
    s = subsets([1, 2, 3])
    assert sorted(map(sorted, s)) == sorted([
        [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
    ])
    assert subsets([]) == [[]]

    # Permutations
    p = permutations([1, 2, 3])
    assert sorted(p) == sorted([
        [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
    ])
    assert permutations([1]) == [[1]]

    # Combination Sum
    c = combination_sum([2, 3, 6, 7], 7)
    assert sorted(map(sorted, c)) == sorted([
        sorted([2, 2, 3]),
        sorted([7]),
    ])
    assert combination_sum([2, 3, 5], 8) == [] or len(combination_sum([2, 3, 5], 8)) == 3

    print("✅ All backtracking drills passed.")
