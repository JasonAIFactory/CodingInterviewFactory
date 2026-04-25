# Array (Python `list`)

**O(1) index access**, O(n) insert/delete in middle.

## 🎯 Essence (memorize this one line)

> *"O of one access by index. Slow to insert in the middle. Default choice for sequence."*

## ✅ Pros / ❌ Cons

- ✅ O(1) random access
- ✅ Cache-friendly
- ❌ O(n) middle insert (shifts elements)

## 🔵 Use when

- Need fast index access
- Sequential processing
- Push/pop at end (stack-like)

## 💡 Trade-off (vs Linked List)

- Array: O(1) access, O(n) middle insert
- Linked list: O(n) access, O(1) insert given reference

## 🇬🇧 What to say

- *"I'll use a list for O of one index access."*
- *"Most operations happen at the end — append is O of one."*
- *"Don't use list.pop(0) — it's O of n. Use deque instead."*
