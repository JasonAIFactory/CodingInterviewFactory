"""
04_sorting_lambda_practice.py  —  TYPE FROM SCRATCH
"""

from collections import Counter


# ============================================================
# 1. sort_by_length(words) -> list[str]
# sort_by_length(["banana", "fig", "apple"]) -> ["fig", "apple", "banana"]
# ============================================================

def sort_by_length(words):
    # TODO: sorted with key=len
    pass


# ============================================================
# 2. sort_descending(nums) -> list[int]
# sort_descending([3, 1, 4, 1, 5]) -> [5, 4, 3, 1, 1]
# ============================================================

def sort_descending(nums):
    # TODO: sorted with reverse=True
    pass


# ============================================================
# 3. sort_people(people) -> list[tuple]
# Sort by name asc, then age asc.
# [("Alice", 30), ("Bob", 25), ("Alice", 25)]
#   -> [("Alice", 25), ("Alice", 30), ("Bob", 25)]
# ============================================================

def sort_people(people):
    # TODO: sorted with key=lambda p: (p[0], p[1])
    pass


# ============================================================
# 4. sort_by_freq_then_alpha(words) -> list[str]
# Frequency desc, alphabetical asc.
# ["a", "b", "a", "c", "b", "a"] -> ["a", "b", "c"]
# ============================================================

def sort_by_freq_then_alpha(words):
    # TODO: counts = Counter(words)
    # TODO: unique = list of unique words
    # TODO: sorted with key=lambda w: (-counts[w], w)
    pass


# ============================================================
# 5. sort_intervals_by_start(intervals) -> list[list[int]]
# [[1, 5], [0, 2], [3, 7]] -> [[0,2],[1,5],[3,7]]
# ============================================================

def sort_intervals_by_start(intervals):
    # TODO: sorted with key=lambda x: x[0]
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    assert sort_by_length(["banana", "fig", "apple"]) == ["fig", "apple", "banana"]
    assert sort_descending([3, 1, 4, 1, 5]) == [5, 4, 3, 1, 1]
    assert sort_people([("Alice", 30), ("Bob", 25), ("Alice", 25)]) \
        == [("Alice", 25), ("Alice", 30), ("Bob", 25)]
    assert sort_by_freq_then_alpha(["a", "b", "a", "c", "b", "a"]) == ["a", "b", "c"]
    assert sort_intervals_by_start([[1, 5], [0, 2], [3, 7]]) == [[0, 2], [1, 5], [3, 7]]
    print("✅ All tests passed.")
