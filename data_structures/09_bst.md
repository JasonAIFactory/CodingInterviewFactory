# BST / Balanced BST

**O(log n) search/insert/delete** when balanced. Python: `sortedcontainers.SortedList`.

## 🎯 Essence (memorize this one line)

> *"Sorted with O of log n operations. Inorder traversal gives sorted output. Hash map is faster but unordered."*

## ✅ Pros / ❌ Cons

- ✅ O(log n) for all ops (balanced)
- ✅ Sorted order via in-order traversal
- ✅ Range queries supported
- ❌ Unbalanced → O(n)
- ❌ No built-in in Python

## 🔵 Use when

- Need sorted order AND fast ops
- Range queries: "values between a and b"
- LeetCode tree problems (LCA, validate BST, diameter)

## 💡 Trade-off (vs Hash Map)

- BST: O(log n), sorted, supports ranges
- Hash map: O(1), unordered
- Pick BST when order matters

## 🇬🇧 What to say

- *"Balanced BST gives O of log n for all operations and sorted iteration."*
- *"Hash map is faster but unordered — pick based on access pattern."*
- *"In Python I'd use SortedList from sortedcontainers."*
