# Graph (Adjacency List or Matrix)

- **Adj List**: O(V + E) space, sparse-friendly
- **Adj Matrix**: O(V²) space, dense-friendly

## 🎯 Essence (memorize this one line)

> *"Adjacency list for sparse graphs, matrix for dense. Most cases use list with defaultdict."*

## ✅ Pros / ❌ Cons

- ✅ Adj list: fast neighbor iteration, less memory
- ✅ Adj matrix: O(1) "is there an edge?"
- ❌ Adj list: O(degree) for edge check
- ❌ Adj matrix: O(V²) space always

## 🔵 Use when

- Adj list → BFS, DFS, Dijkstra (most cases)
- Adj matrix → dense graph, frequent edge checks, Floyd-Warshall

## 💡 Trade-off

- Sparse graph (few edges) → adj list
- Dense graph (E ≈ V²) → adj matrix

## 🇬🇧 What to say

- *"I'll use an adjacency list — O of V plus E, sparse-friendly."*
- *"I build it with defaultdict of list."*
- *"Always confirm directed vs undirected — for undirected, add both directions."*
