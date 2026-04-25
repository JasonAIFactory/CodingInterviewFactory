# Topological Sort

**O(V + E)** — order DAG nodes by dependency.

## 🎯 Essence (memorize this one line)

> *"Order DAG nodes by dependency. Start with zero-indegree nodes, remove and decrement neighbors."*

## 🧠 How it works (principle)

Find an order where every node comes AFTER all its dependencies. **Kahn's algorithm** removes nodes with no remaining dependencies one at a time — when you "process" a node, decrement its neighbors' indegrees, and add any that hit 0 to the queue. Only works on a **DAG** (Directed Acyclic Graph) — a cycle means no valid order exists. If the resulting order is shorter than the node count, you have a cycle.

## 🔵 Use when

- Tasks with prerequisites
- Course Schedule, Build Order
- Detect cycle in directed graph (no topo order = cycle)

## 💡 Two algorithms

- **Kahn's** (BFS-based with indegree tracking)
- **DFS-based** (post-order then reverse, with state coloring)

## 💡 Template (Kahn's — most common)

```python
from collections import defaultdict, deque

graph = defaultdict(list)
indegree = [0] * n
for u, v in edges:        # u must come before v
    graph[u].append(v)
    indegree[v] += 1

queue = deque(i for i in range(n) if indegree[i] == 0)
order = []
while queue:
    node = queue.popleft()
    order.append(node)
    for nb in graph[node]:
        indegree[nb] -= 1
        if indegree[nb] == 0:
            queue.append(nb)

return order if len(order) == n else []   # [] = cycle
```

## 🇬🇧 What to say

- *"Topological sort orders DAG nodes by dependency — O of V plus E."*
- *"I use Kahn's algorithm — start with nodes that have indegree zero."*
- *"If the result length is less than n, the graph has a cycle."*
