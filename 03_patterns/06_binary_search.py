"""
06_binary_search.py  —  REFERENCE FILE

Binary Search template.

Use when:
  - Sorted input → search for value
  - "Find leftmost / rightmost ___"
  - "Minimize / maximize ___ such that condition holds" (binary search on the ANSWER)

Two patterns:
  1. Search a value in a sorted array (canonical)
  2. Binary search on the answer (Koko bananas, capacity, threshold)
"""


# ============================================================
# 1. Canonical — find value in sorted array
# ============================================================

def search(nums: list[int], target: int) -> int:
    """Return index of target, -1 if not present."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ============================================================
# 2. Find leftmost insertion point  (= bisect_left)
# ============================================================

def bisect_left_manual(nums: list[int], target: int) -> int:
    """Smallest index i such that nums[i] >= target."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# ============================================================
# 3. Find rightmost insertion point  (= bisect_right)
# ============================================================

def bisect_right_manual(nums: list[int], target: int) -> int:
    """Smallest index i such that nums[i] > target."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# ============================================================
# 4. Binary search on the ANSWER — Koko Eating Bananas
# ============================================================

def min_eating_speed(piles: list[int], h: int) -> int:
    """
    Find smallest speed k such that Koko can finish all piles in h hours.
    eat(k) = sum(ceil(pile / k))
    """
    def hours_needed(k: int) -> int:
        return sum((pile + k - 1) // k for pile in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            hi = mid                       # try smaller
        else:
            lo = mid + 1                   # need bigger
    return lo


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    print(search([1, 3, 5, 7, 9], 5))                  # 2
    print(search([1, 3, 5, 7, 9], 4))                  # -1
    print(bisect_left_manual([1, 3, 5, 5, 5, 7], 5))   # 2
    print(bisect_right_manual([1, 3, 5, 5, 5, 7], 5))  # 5
    print(min_eating_speed([3, 6, 7, 11], 8))          # 4
    print(min_eating_speed([30, 11, 23, 4, 20], 5))    # 30
    print(min_eating_speed([30, 11, 23, 4, 20], 6))    # 23
