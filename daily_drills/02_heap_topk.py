"""
02_heap_topk.py — Daily drill (type from zero, no peeking)

Target: under 10 minutes.
Patterns: min-heap of size K for top-K largest, tuple sorting in heap.
"""

import heapq


# === Drill 1: K Largest Elements ===
# Return the k largest elements (any order).
# Hint: keep min-heap of size k.
def k_largest(nums: list[int], k: int) -> list[int]:
    pass


# === Drill 2: K Closest Points to Origin ===
# Return k points with smallest Euclidean distance to (0, 0).
# distance squared = x*x + y*y.
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    pass


# === Drill 3: K-th Largest Element in an Array ===
# Return the kth largest (1-indexed: k=1 means the maximum).
def kth_largest(nums: list[int], k: int) -> int:
    pass


# === Tests ===
if __name__ == "__main__":
    # K Largest (order-independent)
    assert sorted(k_largest([3, 2, 1, 5, 6, 4], 2)) == [5, 6]
    assert sorted(k_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)) == [4, 5, 5, 6]

    # K Closest Points
    result = k_closest([[1, 3], [-2, 2]], 1)
    assert result == [[-2, 2]]
    result = k_closest([[3, 3], [5, -1], [-2, 4]], 2)
    assert sorted(map(tuple, result)) == sorted([(3, 3), (-2, 4)])

    # Kth Largest
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert kth_largest([1], 1) == 1

    print("✅ All heap/top-k drills passed.")
