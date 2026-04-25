"""
04_sorting_lambda.py  —  REFERENCE FILE

Goal: Custom sorting with key= and lambda.
This is HUGELY common: sort intervals, sort by frequency, sort tuples.

Two ways to sort in Python:
  - sorted(iterable)      → returns NEW list
  - list.sort()           → sorts IN PLACE, returns None
"""


# ============================================================
# 1. Basic sort with a key
# ============================================================

def sort_by_length(words):
    # SAY: "I pass len as the key. sorted calls key(item) on each item."
    return sorted(words, key=len)


def sort_descending(nums):
    # SAY: "reverse=True flips the order."
    return sorted(nums, reverse=True)


# ============================================================
# 2. Sort by multiple keys using a tuple
# ============================================================

def sort_people(people):
    """
    people = [("Alice", 30), ("Bob", 25), ("Alice", 25)]
    Sort by name ascending, then by age ascending.

    SAY: "When the key returns a tuple, Python compares element by element.
          First by name, and if names tie, by age."
    """
    return sorted(people, key=lambda p: (p[0], p[1]))


def sort_by_freq_then_alpha(words):
    """
    Sort by frequency (descending), break ties alphabetically (ascending).

    SAY: "I want frequency descending and alphabetical ascending.
          To make freq descending while keeping the tie-break ascending,
          I negate the count in the tuple key."
    """
    from collections import Counter
    counts = Counter(words)
    unique = list(counts.keys())
    return sorted(unique, key=lambda w: (-counts[w], w))


# ============================================================
# 3. Sort a list of dicts / objects
# ============================================================

def sort_intervals_by_start(intervals):
    """
    intervals = [[1, 5], [0, 2], [3, 7]]

    SAY: "I sort intervals by their start time.
          This is the first step of most interval problems."
    """
    return sorted(intervals, key=lambda x: x[0])


# ============================================================
# 4. In-place vs new list  —  know the difference
# ============================================================

def in_place_demo():
    nums = [3, 1, 2]
    nums.sort()        # mutates nums, returns None
    print(nums)        # [1, 2, 3]


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    print(sort_by_length(["banana", "fig", "apple"]))    # ['fig', 'apple', 'banana']
    print(sort_descending([3, 1, 4, 1, 5]))              # [5, 4, 3, 1, 1]
    print(sort_people([("Alice", 30), ("Bob", 25), ("Alice", 25)]))
    print(sort_by_freq_then_alpha(["a", "b", "a", "c", "b", "a"]))   # ['a', 'b', 'c']
    print(sort_intervals_by_start([[1, 5], [0, 2], [3, 7]]))         # [[0,2],[1,5],[3,7]]
    in_place_demo()
