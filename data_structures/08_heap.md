# Heap / Priority Queue

**O(log n) push/pop, O(1) peek min.** Python `heapq` is **min-heap only**.

## 🎯 Essence (memorize this one line)

> *"Min or max in O of one. Insert and remove in O of log n. Python heapq is min only — negate for max."*

## ✅ Pros / ❌ Cons

- ✅ O(1) access to min
- ✅ O(log n) insert/remove
- ❌ Only min/max is sorted (no range)
- ❌ O(n) search by value

## 🔵 Use when

- Top K (min-heap of size K)
- Merge K sorted
- Median in stream (two heaps)
- Dijkstra's shortest path

## 💡 Trade-off (vs Sort)

- Heap top-K: **O(n log K)**
- Full sort: **O(n log n)**
- Pick heap when K << n, or for streams

## 🇬🇧 What to say

- *"Min-heap of size K gives top K in O of n log K."*
- *"Better than sorting O of n log n when K is small."*
- *"For max-heap I negate values — Python only has min-heap."*
