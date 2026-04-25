# Union-Find (Disjoint Set Union)

**Near-O(1)** with path compression + union by rank.

## 🎯 Essence (memorize this one line)

> *"Manage disjoint groups. Merge and find in near-O of one with path compression."*

## ✅ Pros / ❌ Cons

- ✅ Near-constant per operation
- ✅ Simple to implement
- ❌ Can't list members of a set easily
- ❌ Can't undo unions

## 🔵 Use when

- Connected components
- "Number of provinces / accounts merge"
- Detect cycle in undirected graph
- Kruskal's MST

## 💡 Trade-off (vs DFS)

- Union-Find: incremental, O(α(n)) per op (effectively O(1))
- DFS: O(V + E) for one full pass

## 🇬🇧 What to say

- *"Union-Find handles dynamic merging in near-O of one."*
- *"Path compression plus union by rank — both required for that speed."*
- *"Inverse Ackermann is effectively constant for any realistic n."*
