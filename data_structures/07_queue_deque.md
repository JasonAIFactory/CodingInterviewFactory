# Queue / Deque (FIFO + double-ended)

**O(1) at both ends.** Python `collections.deque`.

## 🎯 Essence (memorize this one line)

> *"First in, first out. O of one at both ends. Use deque — never list pop zero."*

## ✅ Pros / ❌ Cons

- ✅ O(1) at both ends
- ✅ Perfect for BFS
- ❌ O(n) random access (rarely needed)

## 🔵 Use when

- BFS (queue, FIFO)
- Sliding window max/min (monotonic deque)
- Don't use `list.pop(0)` — that's O(n)

## 💡 Trade-off (vs list)

- Deque: O(1) both ends
- List: O(1) at end only

## 🇬🇧 What to say

- *"I'll use a deque as a FIFO queue — popleft is O of one."*
- *"list.pop(0) would be O of n — that's why deque."*
- *"For sliding window max I use a monotonic deque — O of n total."*
