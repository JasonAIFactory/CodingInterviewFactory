"""
04_sliding_window.py  —  REFERENCE FILE

Sliding Window template.

Use when:
  - "Subarray / substring with constraint ___"
  - "Maximum / minimum / longest / shortest window of ___"

Two flavors:
  - Fixed window  (size k)         — Maximum sum of any k-length window
  - Variable window (expand/shrink) — Longest substring without repeating
"""

from collections import defaultdict


# ============================================================
# 1. Fixed window — max sum of any window of size k
# ============================================================

def max_sum_window(nums: list[int], k: int) -> int:
    """O(n) with sliding sum — never re-scan the window."""
    if k <= 0 or len(nums) < k:
        raise ValueError("Invalid k")

    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]    # add new, remove old
        best = max(best, window_sum)
    return best


# ============================================================
# 2. Variable window — longest substring without repeating chars
# ============================================================

def longest_unique_substring(s: str) -> int:
    """Classic. Expand right, shrink left when duplicate appears."""
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1            # jump left past prior occurrence
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


# ============================================================
# 3. Variable window — minimum window substring containing all chars of t
# ============================================================

def min_window(s: str, t: str) -> str:
    """Find smallest substring of s that contains every char of t (with counts)."""
    if not s or not t:
        return ""

    need: dict[str, int] = defaultdict(int)
    for ch in t:
        need[ch] += 1
    required = len(need)

    have: dict[str, int] = defaultdict(int)
    formed = 0
    left = 0
    best_len = float("inf")
    best_range = (0, 0)

    for right, ch in enumerate(s):
        have[ch] += 1
        if ch in need and have[ch] == need[ch]:
            formed += 1

        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_range = (left, right)

            left_ch = s[left]
            have[left_ch] -= 1
            if left_ch in need and have[left_ch] < need[left_ch]:
                formed -= 1
            left += 1

    return "" if best_len == float("inf") else s[best_range[0]:best_range[1] + 1]


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    print(max_sum_window([2, 1, 5, 1, 3, 2], 3))    # 9
    print(longest_unique_substring("abcabcbb"))     # 3
    print(longest_unique_substring("bbbbb"))        # 1
    print(min_window("ADOBECODEBANC", "ABC"))       # "BANC"
    print(min_window("a", "aa"))                    # ""
