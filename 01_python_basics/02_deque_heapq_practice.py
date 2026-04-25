"""
02_deque_heapq_practice.py  —  TYPE FROM SCRATCH

No peeking at the reference file.
"""

from collections import deque
import heapq


# ============================================================
# 1. bfs_level_order(graph, start) -> list[int]
# Use a deque queue + visited set.
# graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}, start=1
# Expected: [1, 2, 3, 4, 5]
# ============================================================

def bfs_level_order(graph, start):
    # TODO: visited set starting with {start}
    # TODO: queue = deque([start])
    # TODO: order = []
    # TODO: while queue is not empty:
    #         node = queue.popleft()
    #         append to order
    #         for each neighbor of node, if not visited, mark + enqueue
    # TODO: return order
    pass


# ============================================================
# 2. sliding_window_max(nums, k) -> list[int]
# Monotonic deque pattern.
# sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) -> [3, 3, 5, 5, 6, 7]
# ============================================================

def sliding_window_max(nums, k):
    # TODO: dq = deque() to hold indices
    # TODO: result = []
    # TODO: for i, num in enumerate(nums):
    #         pop from front if dq[0] <= i - k  (out of window)
    #         pop from back while nums[dq[-1]] < num  (keep decreasing)
    #         append i
    #         if i >= k - 1: append nums[dq[0]] to result
    # TODO: return result
    pass


# ============================================================
# 3. k_smallest(nums, k) -> list[int]  (sorted ascending)
# k_smallest([5, 2, 8, 1, 9, 3], 3) -> [1, 2, 3]
# ============================================================

def k_smallest(nums, k):
    # TODO: copy nums into heap, heapify it
    # TODO: pop k times, return as list
    pass


# ============================================================
# 4. k_largest(nums, k) -> list[int]  (sorted descending)
# k_largest([5, 2, 8, 1, 9, 3], 3) -> [9, 8, 5]
# ============================================================

def k_largest(nums, k):
    # TODO: maintain a min-heap of size k
    # TODO: push each num, if heap size > k, pop the smallest
    # TODO: return sorted(heap, reverse=True)
    pass


# ============================================================
# 5. k_closest_points(points, k) -> list[list[int]]
# k_closest_points([[1, 1], [2, 2], [0, 1]], 2) -> [[0, 1], [1, 1]]
# ============================================================

def k_closest_points(points, k):
    # TODO: push (distance_squared, point) for each point
    # TODO: pop k smallest, return only the points
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
    assert bfs_level_order(graph, 1) == [1, 2, 3, 4, 5]
    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert k_smallest([5, 2, 8, 1, 9, 3], 3) == [1, 2, 3]
    assert k_largest([5, 2, 8, 1, 9, 3], 3) == [9, 8, 5]
    assert k_closest_points([[1, 1], [2, 2], [0, 1]], 2) == [[0, 1], [1, 1]]
    print("✅ All tests passed.")
