"""
05_two_pointers.py  —  REFERENCE FILE

Two Pointers template.

Use when:
  - Sorted array + find pair / triplet
  - Palindrome / reversal
  - Merge two sorted things
  - Cycle detection in linked list (fast & slow)
  - Remove duplicates in place

Three flavors:
  1. Opposite ends   — l from 0, r from end, move toward each other
  2. Same direction  — slow + fast, both moving forward
  3. Fast & slow     — for cycle detection
"""


# ============================================================
# 1. Opposite ends — Two Sum on a SORTED array
# ============================================================

def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """nums is sorted ascending. Return 1-based indices."""
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left + 1, right + 1]
        if s < target:
            left += 1
        else:
            right -= 1
    return []


# ============================================================
# 2. Opposite ends — Valid Palindrome (alphanumeric, case-insensitive)
# ============================================================

def is_palindrome(s: str) -> bool:
    """Check palindrome ignoring non-alphanumeric and case."""
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


# ============================================================
# 3. Same direction — Remove duplicates from sorted array (in place)
# ============================================================

def remove_duplicates(nums: list[int]) -> int:
    """Return new length; nums modified so first k entries are unique."""
    if not nums:
        return 0
    write = 1                              # next position to write
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


# ============================================================
# 4. Fast & slow — Detect cycle in linked list (Floyd's algorithm)
# ============================================================

class ListNode:
    def __init__(self, val: int, nxt: "ListNode | None" = None):
        self.val = val
        self.next = nxt


def has_cycle(head: ListNode | None) -> bool:
    """O(1) space cycle detection."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next                   # 1 step
        fast = fast.next.next              # 2 steps
        if slow is fast:
            return True
    return False


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))                # [1, 2]
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))                      # False

    nums = [1, 1, 2, 2, 3]
    k = remove_duplicates(nums)
    print(k, nums[:k])                                      # 3 [1, 2, 3]

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b; b.next = c; c.next = a                      # cycle 1-2-3-1
    print(has_cycle(a))                                     # True
