"""
06_binary_search.py — Daily drill (type from zero, no peeking)

Target: under 10 minutes.
Patterns: canonical search, leftmost insert, search on answer.
"""


# === Drill 1: Search in Sorted Array ===
# Return index of target, -1 if not found.
def search(nums: list[int], target: int) -> int:
    pass


# === Drill 2: Leftmost Insertion Point (manual bisect_left) ===
# Smallest i such that nums[i] >= target. May equal len(nums).
def leftmost_insert(nums: list[int], target: int) -> int:
    pass


# === Drill 3: Koko Eating Bananas (search on answer) ===
# piles: list of bananas in each pile. h: hours allowed.
# Each hour Koko eats k bananas from one pile (or fewer if pile smaller).
# Return minimum k such that Koko finishes within h hours.
def min_eating_speed(piles: list[int], h: int) -> int:
    pass


# === Tests ===
if __name__ == "__main__":
    # Search
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([], 5) == -1
    assert search([1], 1) == 0

    # Leftmost insert
    assert leftmost_insert([1, 3, 5, 6], 5) == 2
    assert leftmost_insert([1, 3, 5, 6], 2) == 1
    assert leftmost_insert([1, 3, 5, 6], 7) == 4
    assert leftmost_insert([1, 3, 5, 6], 0) == 0
    assert leftmost_insert([1, 3, 5, 5, 5, 7], 5) == 2

    # Koko Bananas
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23

    print("✅ All binary search drills passed.")
