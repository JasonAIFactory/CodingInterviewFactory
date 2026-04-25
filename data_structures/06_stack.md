# Stack (LIFO)

**O(1) push/pop/peek** at the top. Python `list`.

## 🎯 Essence (memorize this one line)

> *"Last in, first out. O of one at the top. Use Python list."*

## ✅ Pros / ❌ Cons

- ✅ O(1) ops at top
- ✅ Built-in (use `list`)
- ❌ Single end of operation

## 🔵 Use when

- Match brackets / nested structure
- Iterative DFS / tree traversal
- Monotonic stack (Daily Temperatures, Largest Rectangle)
- Undo / redo

## 💡 Trade-off (vs Queue)

- Stack: LIFO — recent first
- Queue: FIFO — earliest first
- Pick based on processing order

## 🇬🇧 What to say

- *"A stack fits because the most recent item is processed first — LIFO."*
- *"I'll use list append and pop — both O of one at the end."*
- *"For monotonic stack, I keep values in increasing or decreasing order and pop when the order breaks."*
