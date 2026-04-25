# BFS (Breadth-First Search)

**O(V + E)** — explore graph level by level.

## 🎯 Essence (memorize this one line)

> *"Explore in rings from the start node. First time we reach the target equals shortest path."*

## 🧠 How it works (principle)

Explore in concentric "rings" from the start node — all neighbors first, then their neighbors, etc. Because BFS always visits closer nodes BEFORE farther ones, the first time we reach a target is via the SHORTEST path (in unweighted graphs). The FIFO queue maintains this level-by-level order. For weighted graphs, BFS doesn't work — use Dijkstra instead.

## 🔵 Use when

- Shortest path in unweighted graph / grid
- Level-order tree traversal
- "Smallest number of steps to ___"

## 💡 Template (graph, shortest path)

```python
from collections import deque

visited = {start}
queue = deque([(start, 0)])
while queue:
    node, dist = queue.popleft()
    if node == target:
        return dist
    for nb in graph[node]:
        if nb not in visited:
            visited.add(nb)
            queue.append((nb, dist + 1))
return -1
```

## 💡 Template (level-by-level)

```python
queue = deque([root])
result = []
while queue:
    level_size = len(queue)
    level = []
    for _ in range(level_size):
        node = queue.popleft()
        level.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    result.append(level)
```

## 🇬🇧 What to say

- *"BFS gives shortest path in unweighted graphs because it expands level by level."*
- *"I use a deque for O of one popleft — list.pop(0) would be O of n."*
- *"Always track visited to avoid revisits and infinite loops."*
