"""
04_sliding_window.py — Daily drill (type from zero, no peeking)

Target: under 10 minutes.
Patterns: variable window with hash map, fixed window sliding sum.
"""


# === Drill 1: Longest Substring Without Repeating Characters ===
# Return length of longest contiguous substring with no duplicate chars.
def longest_unique_substring(s: str) -> int:
    pass


# === Drill 2: Max Sum of Window Size K ===
# Given array of ints and k, return the max sum of any contiguous window of size k.
# Use sliding sum (don't recompute each window).
def max_sum_window(nums: list[int], k: int) -> int:
    pass


# === Drill 3: Longest Substring with At Most K Distinct Chars ===
# Return length of longest contiguous substring with at most k distinct characters.
def longest_at_most_k_distinct(s: str, k: int) -> int:
    pass


# === Tests ===
if __name__ == "__main__":
    # Longest Unique
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("a") == 1

    # Max Sum Window
    assert max_sum_window([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_window([2, 3], 2) == 5
    assert max_sum_window([5], 1) == 5

    # At Most K Distinct
    assert longest_at_most_k_distinct("eceba", 2) == 3   # "ece"
    assert longest_at_most_k_distinct("aa", 1) == 2
    assert longest_at_most_k_distinct("abc", 0) == 0

    print("✅ All sliding window drills passed.")
