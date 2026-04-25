# Step 02 — Input Type & Structure

## 🎯 Purpose
Identify exactly what kind of data you receive.

## 🧠 What interviewer is testing
Whether you understand the data structure space well enough to ask.

## 🇬🇧 English phrases

```
"What is the input type? Is it a list, a string, a tree, or a graph?"
"How is the graph represented? Adjacency list, adjacency matrix, or edge list?"
"Is the linked list singly or doubly linked?"
"Is the tree binary, n-ary, or a binary search tree?"
```

## 📚 Required knowledge

**Common input types and what changes:**

| Input type | What to ask | Why it matters |
|---|---|---|
| **List / array** | Mutable? | In-place ops vs new array |
| **String** | Mutable in your language? | Python strings are immutable |
| **Linked list** | Singly or doubly? | Doubly = O(1) reverse |
| **Tree** | BST? Balanced? n-ary? | BST → O(log n) lookup |
| **Graph** | Directed? Weighted? Adj list / matrix? | Cycles, traversal, Dijkstra need this |
| **Stream** | Can I look back? | One-pass algorithms only |
| **2D grid** | Diagonals count as adjacent? | DFS/BFS direction count |

## 🎯 Selectively-asked — by problem type

Only ask these when the problem involves the matching type:

| If problem involves... | Ask... |
|---|---|
| **Graph** | *"Directed or undirected? Weighted? Adjacency list or matrix? Self-loops? Parallel edges?"* |
| **Tree** | *"Binary or n-ary? Is it a BST? Could nodes have duplicate values?"* |
| **Linked list** | *"Singly or doubly linked? Could there be a cycle?"* |
| **2D grid** | *"Are rows the same length, or jagged? Could rows be empty?"* |
| **Stream / iterator** | *"Can I look back, or single pass only?"* |
| **Matrix** | *"Square only, or rectangular? In-place mutation allowed?"* |

## ⚠️ Common mistakes

- Assuming "graph" = adjacency list (could be matrix)
- Treating tree as graph (don't need visited set for tree DFS)
- Ignoring whether linked list is doubly linked

## 🔁 Drill

For each problem, name 2 questions to ask about the input type:

1. **"Find shortest path from A to B"** → Graph type? Weighted? Directed?
2. **"Reverse a list"** → Array or linked list? If linked, singly or doubly?
3. **"Validate parentheses"** → String? Mutable? Only `()` or also `[]{}`?
