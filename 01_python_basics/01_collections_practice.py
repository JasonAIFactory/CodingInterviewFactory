"""
01_collections_practice.py  —  TYPE FROM SCRATCH

Do NOT look at 01_collections.py while typing.
Run this file. If your output matches the expected output, you passed.

Repeat 3 times in a row without errors before moving on.
"""

from collections import defaultdict, Counter


# ============================================================
# 1. dict basics
# Expected stdout: 3 then 0 then "apple 3"
# ============================================================

def dict_basics():
    # TODO: create an empty dict called `seen`

    # TODO: set seen["apple"] = 3

    # TODO: if "apple" is in seen, print seen["apple"]

    # TODO: use .get to read seen["banana"] with default 0, print it

    # TODO: loop through seen.items() and print key, value
    pass


# ============================================================
# 2. group_words_by_length(words) -> dict[int, list[str]]
# group_words_by_length(["hi", "bye", "ok"]) should return {2: ["hi", "ok"], 3: ["bye"]}
# ============================================================

def group_words_by_length(words):
    # TODO: create a defaultdict(list)
    # TODO: for each word, append it to groups[len(word)]
    # TODO: return groups
    pass


# ============================================================
# 3. count_chars(text) -> dict[str, int]
# count_chars("hello") should return {"h":1, "e":1, "l":2, "o":1}
# ============================================================

def count_chars(text):
    # TODO: create a defaultdict(int)
    # TODO: for each char, increment counts[ch]
    # TODO: return counts
    pass


# ============================================================
# 4. top_k_frequent(words, k) -> list[str]
# top_k_frequent(["a", "b", "a", "c", "b", "a"], 2) should return ["a", "b"]
# ============================================================

def top_k_frequent(words, k):
    # TODO: build a Counter from words
    # TODO: use .most_common(k) and return only the words (not counts)
    pass


# ============================================================
# 5. is_anagram(a, b) -> bool
# is_anagram("listen", "silent") should return True
# is_anagram("abc", "abd") should return False
# ============================================================

def is_anagram(a, b):
    # TODO: compare Counter(a) and Counter(b)
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    dict_basics()
    assert group_words_by_length(["hi", "bye", "ok"]) == {2: ["hi", "ok"], 3: ["bye"]}
    assert count_chars("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert top_k_frequent(["a", "b", "a", "c", "b", "a"], 2) == ["a", "b"]
    assert is_anagram("listen", "silent") is True
    assert is_anagram("abc", "abd") is False
    print("✅ All tests passed.")
