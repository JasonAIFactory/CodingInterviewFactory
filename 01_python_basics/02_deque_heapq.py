"""
02_deque_heapq.py  —  REFERENCE FILE

Goal: Master deque (for BFS) and heapq (for Top-K problems).
These two cover most graph and priority problems at Amazon.
"""

from collections import deque
import heapq


# ============================================================
# 1. deque  —  fast append AND popleft (both O(1))
# ============================================================
# A normal Python list is O(n) when you pop from the front.
# A deque is O(1) on both ends — perfect for BFS queues.

def bfs_level_order(graph, start):
    """
    Standard BFS template using deque.

    SAY: "I use a deque as a FIFO queue.
          I track visited nodes in a set to avoid infinite loops.
          For each node, I explore all neighbors."
    """
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()       # O(1)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def sliding_window_max(nums, k):
    """
    Maximum value in every window of size k.
    Monotonic deque pattern.

    SAY: "I keep a deque of indices where values are decreasing.
          The front is always the max of the current window."
    """
    dq = deque()                     # stores indices
    result = []
    for i, num in enumerate(nums):
        # Remove indices that fall out of the window
        while dq and dq[0] <= i - k:
            dq.popleft()
        # Remove smaller values from the back
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


# ============================================================
# 2. heapq  —  Python only has MIN heap. For max heap, negate values.
# ============================================================

def k_smallest(nums, k):
    """
    SAY: "heapq.heapify turns a list into a min-heap in O(n).
          Then I pop k times — each pop is O(log n)."
    """
    heap = nums[:]           # copy so we don't mutate input
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(k)]


def k_largest(nums, k):
    """
    SAY: "Python's heapq is a min-heap.
          To get the k largest, I keep a min-heap of size k.
          Anything smaller than the top gets pushed out."
    """
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)      # remove the smallest
    return sorted(heap, reverse=True)


def k_closest_points(points, k):
    """
    Return the k points closest to the origin.
    Tuple trick: (distance, point) — heap sorts by the first element.

    SAY: "I push tuples of (distance, point) into a min-heap.
          The smallest distances bubble to the top."
    """
    heap = []
    for x, y in points:
        dist = x * x + y * y         # no need for sqrt
        heapq.heappush(heap, (dist, [x, y]))
    return [heapq.heappop(heap)[1] for _ in range(k)]


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
    print(bfs_level_order(graph, 1))                          # [1, 2, 3, 4, 5]
    print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
    print(k_smallest([5, 2, 8, 1, 9, 3], 3))                  # [1, 2, 3]
    print(k_largest([5, 2, 8, 1, 9, 3], 3))                   # [9, 8, 5]
    print(k_closest_points([[1, 1], [2, 2], [0, 1]], 2))      # [[0, 1], [1, 1]]
