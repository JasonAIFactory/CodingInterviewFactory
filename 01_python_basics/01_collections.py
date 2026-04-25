"""
01_collections.py  —  REFERENCE FILE

Goal: Master dict, defaultdict, and Counter.
These appear in 80%+ of Amazon coding problems.

Read each # SAY: comment OUT LOUD in English.
"""

from collections import defaultdict, Counter


# ============================================================
# 1. dict  —  the most important data structure
# ============================================================

def dict_basics():
    # SAY: "I create an empty hash map."
    seen = {}

    # SAY: "I store the key 'apple' with value 3."
    seen["apple"] = 3

    # SAY: "I check if a key exists in O(1) time."
    if "apple" in seen:
        print(seen["apple"])  # 3

    # SAY: "I use .get with a default value to avoid a KeyError."
    count = seen.get("banana", 0)
    print(count)  # 0

    # SAY: "I iterate over key-value pairs."
    for key, value in seen.items():
        print(key, value)


# ============================================================
# 2. defaultdict  —  no need to check "if key in dict" first
# ============================================================

def group_words_by_length(words):
    """
    Group words by their length.

    SAY: "I use a defaultdict with list as the default factory.
          This way I can append directly without checking if the key exists."
    """
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return groups


def count_chars(text):
    """
    SAY: "I use defaultdict with int as the default.
          Missing keys start at zero, so I can just increment."
    """
    counts = defaultdict(int)
    for ch in text:
        counts[ch] += 1
    return counts


# ============================================================
# 3. Counter  —  built specifically for counting
# ============================================================

def top_k_frequent(words, k):
    """
    Return the k most frequent words.

    SAY: "Counter does the counting for me in one line.
          most_common(k) returns the top k as (word, count) pairs."
    """
    counter = Counter(words)
    return [word for word, _ in counter.most_common(k)]


def is_anagram(a, b):
    """
    SAY: "Two strings are anagrams if their character counts are equal.
          Counter equality is exactly that check."
    """
    return Counter(a) == Counter(b)


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    dict_basics()
    print(group_words_by_length(["hi", "bye", "ok", "yes", "no"]))
    print(count_chars("hello"))
    print(top_k_frequent(["a", "b", "a", "c", "b", "a"], 2))
    print(is_anagram("listen", "silent"))
