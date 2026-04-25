"""
06_binary_search_practice.py  —  TYPE FROM SCRATCH
"""


# ============================================================
# 1. search(nums, target) -> int   (-1 if not found)
# ============================================================

def search(nums, target):
    # TODO: lo, hi = 0, len-1
    # TODO: while lo <= hi: mid; if equal return; if less, lo = mid+1; else hi = mid-1
    pass


# ============================================================
# 2. bisect_left_manual(nums, target) -> int   (insertion point)
# ============================================================

def bisect_left_manual(nums, target):
    # TODO: lo = 0, hi = len(nums)  (exclusive!)
    # TODO: while lo < hi: mid; if nums[mid] < target: lo=mid+1 else hi=mid
    pass


# ============================================================
# 3. bisect_right_manual(nums, target) -> int
# ============================================================

def bisect_right_manual(nums, target):
    # TODO: same as left, but condition is nums[mid] <= target
    pass


# ============================================================
# 4. min_eating_speed(piles, h) -> int   (Koko bananas)
# ============================================================

def min_eating_speed(piles, h):
    # TODO: helper hours_needed(k) = sum of ceil(pile / k) = sum((pile + k - 1) // k)
    # TODO: binary search on k from 1 to max(piles)
    # TODO: if feasible at mid, try smaller (hi = mid); else lo = mid + 1
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    assert search([1, 3, 5, 7, 9], 5) == 2
    assert search([1, 3, 5, 7, 9], 4) == -1
    assert search([], 1) == -1
    assert bisect_left_manual([1, 3, 5, 5, 5, 7], 5) == 2
    assert bisect_right_manual([1, 3, 5, 5, 5, 7], 5) == 5
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    print("✅ All tests passed.")
