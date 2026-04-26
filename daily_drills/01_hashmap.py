"""
01_hashmap.py — Daily drill (type from zero, no peeking)

Target: under 8 minutes.
Patterns: hash map for O(1) lookup, anagram key trick.
"""

from collections import defaultdict


# === Drill 1: Two Sum ===
# Return indices of two numbers that sum to target.
# Assume exactly one valid pair exists.
def two_sum(nums: list[int], target: int) -> list[int]:
    pass


# === Drill 2: Group Anagrams ===
# Group strings that are anagrams of each other.
# Anagrams = same letters, different order.
def group_anagrams(strs: list[str]) -> list[list[str]]:
    pass


# === Drill 3: First Non-Repeating Character ===
# Return index of first character that appears only once.
# Return -1 if none.
def first_unique_char(s: str) -> int:
    pass


# === Tests ===
if __name__ == "__main__":
    # Two Sum
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Group Anagrams
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(map(sorted, result)) == sorted([
        sorted(["bat"]),
        sorted(["nat", "tan"]),
        sorted(["ate", "eat", "tea"]),
    ])
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]

    # First Unique Char
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert first_unique_char("") == -1

    print("✅ All hashmap drills passed.")
