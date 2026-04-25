# Step 11 — State the Brute Force First

## 🎯 Purpose
Even if you know the optimal — propose the obvious, slow solution first.

## 🧠 What interviewer is testing
- Can you find ANY solution before optimizing?
- Are you a human (who explores) or a memorized-answer machine?

## 🇬🇧 English phrases

```
"My first thought is brute force."
"For each element, I would check every other element."
"The naive approach is to try every possible combination."
"This gives us O(?) time and O(?) space. It works, but I think we can do better."
```

## 📚 Required knowledge — common brute force patterns

| Problem type | Brute force |
|---|---|
| Find pair | Nested loop, O(n²) |
| Find triplet | Triple loop, O(n³) |
| All subsets | Recursive enumerate, O(2ⁿ) |
| All permutations | Backtracking, O(n!) |
| All paths in graph | DFS from every node, exponential |
| String matching | Compare at every starting index, O(n·m) |
| Find min/max in subarray | Re-scan each window, O(n·k) |

## 🔑 The script

> *"The brute force is to **[do X for every Y]**. That gives O(?) time and O(?) space. It works, but I think we can improve it by avoiding **[repeated work / redundant computation]**."*

## ⚠️ Common mistakes

- Skipping straight to optimal → sounds rehearsed, no thinking shown
- Brute force without stating its complexity
- Saying "brute force is O(n²)" without explaining WHY

## 🔁 Drill

For each, state brute force in one sentence + complexity:

1. **"Find two numbers summing to target"** → Try every pair: O(n²) time, O(1) space.
2. **"Longest substring without repeating chars"** → Try every substring, check uniqueness: O(n³).
3. **"Find shortest path in unweighted graph"** → DFS from source, return min over all paths: exponential.
