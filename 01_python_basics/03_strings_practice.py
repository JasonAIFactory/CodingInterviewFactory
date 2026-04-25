"""
03_strings_practice.py  —  TYPE FROM SCRATCH
"""


# ============================================================
# 1. reverse_string(s) -> str
# reverse_string("hello") -> "olleh"
# ============================================================

def reverse_string(s):
    # TODO: use slicing s[::-1]
    pass


# ============================================================
# 2. char_to_index(ch) -> int
# char_to_index("a") -> 0, char_to_index("z") -> 25
# ============================================================

def char_to_index(ch):
    # TODO: return ord(ch) - ord("a")
    pass


# ============================================================
# 3. reverse_words(sentence) -> str
# reverse_words("hello amazon interview") -> "interview amazon hello"
# ============================================================

def reverse_words(sentence):
    # TODO: split, reverse list, join with " "
    pass


# ============================================================
# 4. is_palindrome(s) -> bool   (case-insensitive, alphanumeric only)
# is_palindrome("A man, a plan, a canal: Panama") -> True
# is_palindrome("race a car") -> False
# ============================================================

def is_palindrome(s):
    # TODO: build cleaned = lowercase alphanumeric chars only
    # TODO: return cleaned == cleaned[::-1]
    pass


# ============================================================
# 5. count_letters(s) -> dict[str, int]   (only letters, lowercase counted)
# count_letters("Hello!") -> {"h":1, "e":1, "l":2, "o":1}
# ============================================================

def count_letters(s):
    # TODO: iterate, only count s if ch.isalpha(), lowercase the key
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert char_to_index("a") == 0
    assert char_to_index("z") == 25
    assert reverse_words("hello amazon interview") == "interview amazon hello"
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert count_letters("Hello!") == {"h": 1, "e": 1, "l": 2, "o": 1}
    print("✅ All tests passed.")
