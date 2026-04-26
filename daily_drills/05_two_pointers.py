"""
05_two_pointers.py — Daily drill (type from zero, no peeking)

Target: under 12 minutes.
Patterns: opposite ends, fast/slow, sort + two pointers.
"""


# === Drill 1: Valid Palindrome ===
# Ignore non-alphanumeric chars, case-insensitive.
def is_palindrome(s: str) -> bool:
    pass


# === Drill 2: 3Sum ===
# Return all unique triplets [a, b, c] where a + b + c == 0.
# Sort + two pointers approach.
def three_sum(nums: list[int]) -> list[list[int]]:
    pass


# === Drill 3: Container With Most Water ===
# Return max water area. Move the SHORTER side inward.
def max_area(height: list[int]) -> int:
    pass


# === Drill 4: Has Cycle (Linked List, Floyd's tortoise & hare) ===
class ListNode:
    def __init__(self, val: int, nxt: "ListNode | None" = None):
        self.val = val
        self.next = nxt


def has_cycle(head: ListNode | None) -> bool:
    pass


# === Tests ===
if __name__ == "__main__":
    # Palindrome
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome("") is True
    assert is_palindrome(".,") is True

    # 3Sum
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert sorted(map(sorted, result)) == sorted([[-1, -1, 2], [-1, 0, 1]])
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([1, 2, 3]) == []

    # Container
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16

    # Has Cycle
    a, b, c = ListNode(1), ListNode(2), ListNode(3)
    a.next = b; b.next = c; c.next = a
    assert has_cycle(a) is True

    x = ListNode(1, ListNode(2, ListNode(3)))
    assert has_cycle(x) is False
    assert has_cycle(None) is False

    print("✅ All two pointers drills passed.")
