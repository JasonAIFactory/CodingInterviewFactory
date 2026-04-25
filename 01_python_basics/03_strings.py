"""
03_strings.py  —  REFERENCE FILE

Goal: Master string manipulation.
Strings appear in roughly 1/3 of all coding problems (palindrome, anagram,
parsing, sliding window on text, etc.).

Key fact: Python strings are IMMUTABLE.
You cannot do s[0] = "x". You build a new string instead.
"""


# ============================================================
# 1. Slicing  —  the most powerful string tool in Python
# ============================================================

def slicing_basics():
    s = "interview"

    # SAY: "Slicing creates a new string. The end index is exclusive."
    print(s[0:4])      # "inte"
    print(s[4:])       # "rview"
    print(s[:4])       # "inte"
    print(s[-3:])      # "iew"   (last 3 chars)
    print(s[::-1])     # "weivretni"  ← REVERSE TRICK


# ============================================================
# 2. split and join  —  use these instead of manual loops
# ============================================================

def split_join_basics():
    sentence = "hello amazon interview"

    # SAY: "split returns a list of words."
    words = sentence.split(" ")        # ["hello", "amazon", "interview"]

    # SAY: "join builds a string from a list with a separator."
    rejoined = "-".join(words)         # "hello-amazon-interview"
    print(rejoined)


# ============================================================
# 3. Character checks and ord/chr
# ============================================================

def char_checks(ch):
    # SAY: "isdigit, isalpha, isalnum are O(1) character checks."
    return {
        "is_digit": ch.isdigit(),
        "is_alpha": ch.isalpha(),
        "is_alnum": ch.isalnum(),
        "is_lower": ch.islower(),
    }


def char_to_index(ch):
    """
    Map a lowercase letter to 0..25.

    SAY: "ord gives the Unicode code point.
          Subtracting ord('a') normalizes letters to indices."
    """
    return ord(ch) - ord("a")


def index_to_char(i):
    # SAY: "chr is the inverse of ord."
    return chr(ord("a") + i)


# ============================================================
# 4. Building a string  —  use a list, then join
# ============================================================

def reverse_words(sentence):
    """
    SAY: "I split into words, reverse the list, and join with a space.
          This is O(n) total."
    """
    return " ".join(sentence.split()[::-1])


def is_palindrome(s):
    """
    Ignore case and non-alphanumeric characters.

    SAY: "I clean the string into lowercase letters and digits only,
          then compare it to its reverse."
    """
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


# ============================================================
# 5. Building strings the WRONG way (avoid in tight loops)
# ============================================================
# Bad:   result = ""; result += ch        -> O(n^2) total
# Good:  parts = []; parts.append(ch); "".join(parts)   -> O(n)


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    slicing_basics()
    split_join_basics()
    print(char_checks("a"))
    print(char_to_index("c"))                   # 2
    print(index_to_char(2))                     # "c"
    print(reverse_words("hello amazon interview"))
    print(is_palindrome("A man, a plan, a canal: Panama"))   # True
    print(is_palindrome("race a car"))                       # False
