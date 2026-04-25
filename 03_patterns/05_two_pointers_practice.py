"""
05_two_pointers_practice.py  —  TYPE FROM SCRATCH
"""


# ============================================================
# 1. two_sum_sorted(nums, target) -> list[int]   (1-based indices)
# two_sum_sorted([2, 7, 11, 15], 9) -> [1, 2]
# ============================================================

def two_sum_sorted(nums, target):
    # TODO: left, right pointers
    # TODO: while left < right: compute sum, move pointers based on comparison
    pass


# ============================================================
# 2. is_palindrome(s) -> bool   (alphanumeric only, case-insensitive)
# is_palindrome("A man, a plan, a canal: Panama") -> True
# ============================================================

def is_palindrome(s):
    # TODO: left, right
    # TODO: skip non-alnum on both sides
    # TODO: compare lowercased chars
    pass


# ============================================================
# 3. remove_duplicates(nums) -> int   (in place; returns new length)
# nums = [1, 1, 2, 2, 3] -> returns 3, nums[:3] == [1, 2, 3]
# ============================================================

def remove_duplicates(nums):
    # TODO: handle empty
    # TODO: write index starts at 1
    # TODO: for each read pos, if differs from previous, write and advance
    pass


# ============================================================
# 4. ListNode + has_cycle(head) -> bool   (Floyd's tortoise & hare)
# ============================================================

class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


def has_cycle(head):
    # TODO: slow = fast = head
    # TODO: while fast and fast.next: slow = slow.next; fast = fast.next.next; if equal return True
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False

    nums = [1, 1, 2, 2, 3]
    k = remove_duplicates(nums)
    assert k == 3
    assert nums[:k] == [1, 2, 3]

    a = ListNode(1); b = ListNode(2); c = ListNode(3)
    a.next = b; b.next = c; c.next = a
    assert has_cycle(a) is True

    # No cycle
    x = ListNode(1, ListNode(2, ListNode(3)))
    assert has_cycle(x) is False

    print("✅ All tests passed.")
