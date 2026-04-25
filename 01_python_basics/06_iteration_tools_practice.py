"""
06_iteration_tools_practice.py  —  TYPE FROM SCRATCH
"""


# ============================================================
# 1. squares_of_evens(nums) -> list[int]
# squares_of_evens([1, 2, 3, 4, 5]) -> [4, 16]
# ============================================================

def squares_of_evens(nums):
    # TODO: list comprehension with if filter
    pass


# ============================================================
# 2. name_to_length(names) -> dict[str, int]
# name_to_length(["Alice", "Bob"]) -> {"Alice": 5, "Bob": 3}
# ============================================================

def name_to_length(names):
    # TODO: dict comprehension
    pass


# ============================================================
# 3. unique_lengths(words) -> set[int]
# unique_lengths(["hi", "ok", "bye"]) -> {2, 3}
# ============================================================

def unique_lengths(words):
    # TODO: set comprehension
    pass


# ============================================================
# 4. make_matrix(rows, cols) -> list[list[int]]   (filled with 0)
# make_matrix(2, 3) -> [[0,0,0],[0,0,0]]
# ============================================================

def make_matrix(rows, cols):
    # TODO: nested list comprehension
    pass


# ============================================================
# 5. flatten(matrix) -> list[int]
# flatten([[1, 2], [3, 4]]) -> [1, 2, 3, 4]
# ============================================================

def flatten(matrix):
    # TODO: [x for row in matrix for x in row]
    pass


# ============================================================
# 6. zip_to_dict(keys, values) -> dict
# zip_to_dict(["a", "b"], [1, 2]) -> {"a": 1, "b": 2}
# ============================================================

def zip_to_dict(keys, values):
    # TODO: dict(zip(keys, values))
    pass


# ============================================================
# 7. enumerate_indices_of(target, items) -> list[int]
# enumerate_indices_of("a", ["a", "b", "a", "c"]) -> [0, 2]
# ============================================================

def enumerate_indices_of(target, items):
    # TODO: list comprehension over enumerate
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    assert squares_of_evens([1, 2, 3, 4, 5]) == [4, 16]
    assert name_to_length(["Alice", "Bob"]) == {"Alice": 5, "Bob": 3}
    assert unique_lengths(["hi", "ok", "bye"]) == {2, 3}
    assert make_matrix(2, 3) == [[0, 0, 0], [0, 0, 0]]
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert zip_to_dict(["a", "b"], [1, 2]) == {"a": 1, "b": 2}
    assert enumerate_indices_of("a", ["a", "b", "a", "c"]) == [0, 2]
    print("✅ All tests passed.")
