"""
05_bisect_practice.py  —  TYPE FROM SCRATCH
"""

import bisect


# ============================================================
# 1. find_index(sorted_arr, x) -> int   (-1 if not found)
# find_index([1, 3, 5, 5, 5, 7, 9], 5) -> 2
# find_index([1, 3, 5, 5, 5, 7, 9], 4) -> -1
# ============================================================

def find_index(sorted_arr, x):
    # TODO: i = bisect_left(sorted_arr, x)
    # TODO: if i < len(arr) and arr[i] == x, return i, else -1
    pass


# ============================================================
# 2. insert_sorted(sorted_arr, x) -> list  (mutates AND returns)
# insert_sorted([1, 3, 7], 5) -> [1, 3, 5, 7]
# ============================================================

def insert_sorted(sorted_arr, x):
    # TODO: bisect.insort(sorted_arr, x); return sorted_arr
    pass


# ============================================================
# 3. count_in_range(sorted_arr, low, high) -> int
# count_in_range([1, 3, 5, 5, 5, 7, 9], 3, 7) -> 5
# ============================================================

def count_in_range(sorted_arr, low, high):
    # TODO: left = bisect_left for low
    # TODO: right = bisect_right for high
    # TODO: return right - left
    pass


# ============================================================
# 4. first_greater_or_equal(sorted_arr, target) -> int | None
# first_greater_or_equal([1, 3, 5, 7, 9], 6) -> 7
# first_greater_or_equal([1, 3, 5, 7, 9], 10) -> None
# ============================================================

def first_greater_or_equal(sorted_arr, target):
    # TODO: i = bisect_left(sorted_arr, target)
    # TODO: if i == len, return None, else return arr[i]
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 7, 9]
    assert find_index(arr, 5) == 2
    assert find_index(arr, 4) == -1
    assert insert_sorted([1, 3, 7], 5) == [1, 3, 5, 7]
    assert count_in_range(arr, 3, 7) == 5
    assert first_greater_or_equal(arr, 6) == 7
    assert first_greater_or_equal(arr, 10) is None
    print("✅ All tests passed.")
