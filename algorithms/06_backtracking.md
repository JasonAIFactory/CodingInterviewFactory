# Backtracking

**O(2^n) or O(n!)** — explore all possibilities, undo when invalid.

## 🎯 Essence (memorize this one line)

> *"Try a choice, recurse, then undo. Prune dead branches early."*

## 🧠 How it works (principle)

Build solutions incrementally — make a choice, recurse to extend, then UNDO the choice (backtrack) to try alternatives. The recursion stack tracks the current "path" being built. **Pruning** is what makes this practical: as soon as a partial solution can't lead to a valid result, abandon that branch. Without pruning, backtracking is just brute-force enumeration.

## 🔵 Use when

- All subsets / permutations / combinations
- "Find all valid configurations of ___"
- Word Search, N-Queens, Sudoku, Combination Sum

## 💡 Universal template

```python
def backtrack(path, choices):
    if base_case_met:
        result.append(path[:])      # SNAPSHOT — important!
        return
    for choice in choices:
        path.append(choice)         # make
        backtrack(path, next_choices)
        path.pop()                  # undo
```

## 💡 Template (subsets)

```python
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
```

## 💡 Template (permutations)

```python
def permutations(nums):
    result = []
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    backtrack([], [False] * len(nums))
    return result
```

## 🇬🇧 What to say

- *"Backtracking explores all possibilities and undoes choices."*
- *"I append a slice of path to result — that's a snapshot, not a reference."*
- *"Prune early to avoid exploring invalid branches."*
