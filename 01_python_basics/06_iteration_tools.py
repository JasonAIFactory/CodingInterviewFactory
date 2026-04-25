"""
06_iteration_tools.py  —  REFERENCE FILE

Goal: Master enumerate, zip, comprehensions.
These make code SHORTER and CLEANER — that's Logical & Maintainable points.
"""


# ============================================================
# 1. enumerate  —  index AND value at the same time
# ============================================================

def enumerate_basics():
    items = ["a", "b", "c"]

    # SAY: "enumerate gives me both the index and the value.
    #       I avoid manual index tracking with i = 0; i += 1."
    for i, item in enumerate(items):
        print(i, item)

    # SAY: "I can start from a different number with start=."
    for i, item in enumerate(items, start=1):
        print(i, item)


# ============================================================
# 2. zip  —  iterate two lists in parallel
# ============================================================

def zip_basics():
    names = ["Alice", "Bob", "Carol"]
    ages = [30, 25, 40]

    # SAY: "zip pairs elements from each iterable.
    #       It stops at the shortest one."
    for name, age in zip(names, ages):
        print(name, age)

    # SAY: "I can build a dict from two parallel lists in one line."
    name_to_age = dict(zip(names, ages))
    print(name_to_age)


# ============================================================
# 3. List / dict / set comprehensions
# ============================================================

def squares_of_evens(nums):
    # SAY: "List comprehension: [expression for item in iterable if condition]."
    return [n * n for n in nums if n % 2 == 0]


def name_to_length(names):
    # SAY: "Dict comprehension: {key: value for ... in ...}."
    return {name: len(name) for name in names}


def unique_lengths(words):
    # SAY: "Set comprehension uses braces with a single expression."
    return {len(w) for w in words}


# ============================================================
# 4. Nested comprehension for 2D
# ============================================================

def make_matrix(rows, cols):
    """
    Build a rows x cols matrix of zeros.

    SAY: "I write the inner list first, then the outer.
          Read it left-to-right as: for each row, build a row of zeros."
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]


def flatten(matrix):
    """
    SAY: "Nested comprehension: outer loop first, inner loop second."
    """
    return [x for row in matrix for x in row]


# ============================================================
# 5. Generator expression  —  same syntax with parentheses, lazy
# ============================================================

def sum_of_squares(nums):
    """
    SAY: "Generator does not build a full list in memory.
          It produces values one at a time. Better for large inputs."
    """
    return sum(n * n for n in nums)


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    enumerate_basics()
    zip_basics()
    print(squares_of_evens([1, 2, 3, 4, 5]))         # [4, 16]
    print(name_to_length(["Alice", "Bob"]))          # {"Alice": 5, "Bob": 3}
    print(unique_lengths(["hi", "ok", "bye"]))       # {2, 3}
    print(make_matrix(2, 3))                         # [[0,0,0],[0,0,0]]
    print(flatten([[1, 2], [3, 4]]))                 # [1, 2, 3, 4]
    print(sum_of_squares([1, 2, 3]))                 # 14
