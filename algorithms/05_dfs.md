# DFS (Depth-First Search)

**O(V + E)** — explore deep before wide.

## 🎯 Essence (memorize this one line)

> *"Go as deep as possible first. Backtrack when stuck. Good for paths, components, and tree traversal."*

## 🧠 How it works (principle)

Go as deep as possible down one branch before backtracking. The recursion stack (or explicit stack for iterative) implicitly tracks the current path. Naturally suited for: enumerating ALL paths, finding ANY path, tree traversals, cycle detection. Each node is visited at most once when you track `visited`.

## 🔵 Use when

- All paths / all combinations
- Connected components count
- Tree traversal (preorder / inorder / postorder) — see section below
- Detect cycle (with state coloring)

## 💡 Template (recursive)

```python
def dfs(node):
    if node in visited:
        return
    visited.add(node)
    # process node
    for nb in graph[node]:
        dfs(nb)
```

## 💡 Template (iterative)

```python
stack = [start]
visited = set()
while stack:
    node = stack.pop()
    if node in visited:
        continue
    visited.add(node)
    for nb in graph[node]:
        if nb not in visited:
            stack.append(nb)
```

## 💡 Template (tree DFS — return value)

```python
def max_depth(node):
    if node is None:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

## 🌳 Tree Traversals (DFS variants)

Three orders depending on **WHEN you visit the root**:

| Traversal | Visit order | Use case |
|---|---|---|
| **Preorder** | root → left → right | Serialize / copy tree, prefix expression |
| **Inorder** | left → root → right | Sorted output from BST |
| **Postorder** | left → right → root | Delete tree, postfix eval, child-first computation |

### 💡 Recursive templates (one-liners)

```python
def preorder(node):
    if not node: return []
    return [node.val] + preorder(node.left) + preorder(node.right)

def inorder(node):
    if not node: return []
    return inorder(node.left) + [node.val] + inorder(node.right)

def postorder(node):
    if not node: return []
    return postorder(node.left) + postorder(node.right) + [node.val]
```

### 💡 Iterative inorder (classic interview)

```python
def inorder_iter(root):
    result, stack = [], []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result
```

### 🇬🇧 What to say (tree traversals)

- *"Preorder visits root first — useful for serializing or copying a tree."*
- *"Inorder on a BST returns values in sorted order — that's the BST invariant."*
- *"Postorder visits root last — useful when the root computation depends on children, like deleting a tree or evaluating expressions."*

## 🇬🇧 What to say (general DFS)

- *"DFS goes deep first — better for finding all paths or for tree traversal."*
- *"Recursive is cleaner but risks stack overflow on deep input — I'd switch to iterative if depth could be large."*
- *"For graph DFS I always need a visited set to avoid revisits."*
