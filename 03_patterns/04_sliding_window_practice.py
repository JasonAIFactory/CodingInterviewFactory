"""
04_sliding_window_practice.py  —  TYPE FROM SCRATCH
"""

from collections import defaultdict


# ============================================================
# 1. max_sum_window(nums, k) -> int
# max_sum_window([2, 1, 5, 1, 3, 2], 3) -> 9
# ============================================================

def max_sum_window(nums, k):
    # TODO: validate k > 0 and len >= k
    # TODO: window_sum = sum first k; best = window_sum
    # TODO: slide: window_sum += nums[i] - nums[i - k]; update best
    pass


# ============================================================
# 2. longest_unique_substring(s) -> int
# longest_unique_substring("abcabcbb") -> 3
# ============================================================

def longest_unique_substring(s):
    # TODO: last_seen = {}; left = 0; best = 0
    # TODO: for right, ch in enumerate(s):
    #         if ch in last_seen and last_seen[ch] >= left: left = last_seen[ch] + 1
    #         last_seen[ch] = right
    #         best = max(best, right - left + 1)
    pass


# ============================================================
# 3. min_window(s, t) -> str
# min_window("ADOBECODEBANC", "ABC") -> "BANC"
# ============================================================

def min_window(s, t):
    # TODO: empty check
    # TODO: need = Counter of t; required = number of distinct chars
    # TODO: have = defaultdict(int); formed = 0; left = 0
    # TODO: track best_len and best_range
    # TODO: expand right; when formed == required, shrink left and update best
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    assert max_sum_window([2, 1, 5, 1, 3, 2], 3) == 9
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("") == 0
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "aa") == ""
    print("✅ All tests passed.")
