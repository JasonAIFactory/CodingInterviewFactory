"""
05_bisect.py  —  REFERENCE FILE

Goal: Binary search using the bisect module.
This converts O(n) lookups into O(log n) on a SORTED list.

Two functions to know:
  - bisect_left(arr, x)  → insertion point for x, leftmost position
  - bisect_right(arr, x) → insertion point for x, rightmost position

Key intuition:
  arr =       [1, 3, 5, 5, 5, 7]
  bisect_left(arr, 5)  -> 2   (before the first 5)
  bisect_right(arr, 5) -> 5   (after the last 5)
"""

import bisect


# ============================================================
# 1. Find an element's position
# ============================================================

def find_index(sorted_arr, x):
    """
    Return the index of x in a sorted list, or -1 if not found.

    SAY: "bisect_left finds where x would go, leftmost.
          If the value at that position is x, the element exists."
    """
    i = bisect.bisect_left(sorted_arr, x)
    if i < len(sorted_arr) and sorted_arr[i] == x:
        return i
    return -1


# ============================================================
# 2. Insert while keeping the list sorted
# ============================================================

def insert_sorted(sorted_arr, x):
    """
    SAY: "bisect.insort inserts x while preserving sort order.
          The lookup is O(log n), but the actual insert is O(n)
          because list elements have to shift."
    """
    bisect.insort(sorted_arr, x)
    return sorted_arr


# ============================================================
# 3. Count elements in a range using bisect
# ============================================================

def count_in_range(sorted_arr, low, high):
    """
    Count elements where low <= x <= high.

    SAY: "I find the leftmost position for low and the rightmost for high.
          The difference is the count, in O(log n)."
    """
    left = bisect.bisect_left(sorted_arr, low)
    right = bisect.bisect_right(sorted_arr, high)
    return right - left


# ============================================================
# 4. Find the smallest element >= target
# ============================================================

def first_greater_or_equal(sorted_arr, target):
    """
    SAY: "bisect_left gives me the index of the first element >= target.
          If the index is past the end, no such element exists."
    """
    i = bisect.bisect_left(sorted_arr, target)
    if i == len(sorted_arr):
        return None
    return sorted_arr[i]


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 7, 9]
    print(find_index(arr, 5))                # 2
    print(find_index(arr, 4))                # -1
    print(insert_sorted([1, 3, 7], 5))       # [1, 3, 5, 7]
    print(count_in_range(arr, 3, 7))         # 5  (3, 5, 5, 5, 7)
    print(first_greater_or_equal(arr, 6))    # 7
    print(first_greater_or_equal(arr, 10))   # None
