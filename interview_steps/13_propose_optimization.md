# Step 13 — Propose Optimization + Justify Data Structure

## 🎯 Purpose
Name the optimal approach AND explain WHY that data structure fits.

## 🧠 What interviewer is testing
Data-structure intuition. Can you map "problem signal → right tool"?

## 🇬🇧 English phrases

```
"If I use a hash map to store seen values, I can do the lookup in O(1)."
"A heap gives me the top-k in O(n log k) — better than sorting in O(n log n)."
"Since the input is sorted, I can use binary search for O(log n) lookup."
"Two pointers will work here because the array is sorted."
"BFS makes sense because we want the shortest path in an unweighted graph."
```

## 📚 Required knowledge — Problem signal → Data structure

| Problem signal | Use this | Why |
|---|---|---|
| "Find pair summing to k" | Hash map | O(1) complement lookup |
| "Top k / k-th smallest" | Heap of size k | O(n log k) |
| "Need fast min/max in window" | Monotonic deque | O(n) total |
| "Already sorted, find element" | Binary search | O(log n) |
| "Shortest path, unweighted" | BFS | Level by level |
| "Shortest path, weighted positive" | Dijkstra (heap) | Greedy + priority |
| "All paths / all combinations" | Backtracking (DFS) | Explore + prune |
| "Counting subproblems" | DP (memo or table) | Avoid recomputation |
| "Connected components" | Union-Find or BFS/DFS | Group merging |
| "Schedule / dependency" | Topological sort | DAG ordering |
| "Range sum queries" | Prefix sum array | O(1) range query after O(n) prep |
| "Frequency counting" | Counter / dict | O(1) per update |
| "Recently used / LRU" | Hash map + doubly linked list | O(1) get/put |
| "Match brackets" | Stack | LIFO order |

## 🔑 The script

> *"The signal here is **[problem feature]**.
> The right data structure is **[X]** because **[property]**.
> This brings the complexity to O(?)."*

## ⚠️ Common mistakes

- Naming the structure without justifying it ("I'll use a hash map" — why?)
- Picking sort when hash map suffices
- Picking DP when greedy works

## 🔁 Drill

For each problem signal, name the data structure + why:

1. **"Find median in a stream"** → Two heaps (max-heap left, min-heap right) — keep balance for O(log n) insert, O(1) median.
2. **"Detect cycle in linked list"** → Two pointers (Floyd's tortoise & hare) — O(1) extra space.
3. **"Most frequent k words"** → Counter + heap (or `Counter.most_common(k)`).
