"""
09_oop_core.py — Daily drill (type from zero, no peeking)

Target: under 15 minutes.
Patterns: ListNode + reverse, TreeNode + traversals, MinStack, mini LRU.
"""


# === Drill 1: ListNode + Reverse Linked List (iterative) ===
class ListNode:
    def __init__(self, val: int, nxt: "ListNode | None" = None):
        self.val = val
        self.next = nxt


def reverse_list(head: ListNode | None) -> ListNode | None:
    pass


# === Drill 2: TreeNode + Tree Traversals ===
class TreeNode:
    def __init__(self, val: int, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode | None) -> list[int]:
    """root, left, right"""
    pass


def inorder(root: TreeNode | None) -> list[int]:
    """left, root, right (sorted output for BST)"""
    pass


def postorder(root: TreeNode | None) -> list[int]:
    """left, right, root"""
    pass


# === Drill 3: MinStack ===
# push, pop, top, getMin — all O(1).
# Hint: parallel stack of running minimums.
class MinStack:
    def __init__(self) -> None:
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


# === Drill 4: LRU Cache (mini — using OrderedDict shortcut) ===
# get, put — both O(1) amortized.
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int) -> None:
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


# === Tests ===
if __name__ == "__main__":
    # Reverse Linked List
    def to_list(node):
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return out

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert to_list(reverse_list(head)) == [5, 4, 3, 2, 1]
    assert reverse_list(None) is None
    assert to_list(reverse_list(ListNode(1))) == [1]

    # Tree Traversals
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert preorder(root) == [1, 2, 4, 5, 3]
    assert inorder(root) == [4, 2, 5, 1, 3]
    assert postorder(root) == [4, 5, 2, 3, 1]
    assert preorder(None) == []

    # MinStack
    s = MinStack()
    s.push(-2); s.push(0); s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2

    # LRU Cache
    c = LRUCache(2)
    c.put(1, 100)
    c.put(2, 200)
    assert c.get(1) == 100
    c.put(3, 300)              # evicts 2
    assert c.get(2) == -1
    c.put(4, 400)              # evicts 1
    assert c.get(1) == -1
    assert c.get(3) == 300
    assert c.get(4) == 400

    print("✅ All OOP core drills passed.")
