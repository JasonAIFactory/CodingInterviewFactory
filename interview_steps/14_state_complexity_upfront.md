# Step 14 — State Complexity BEFORE Coding

## 🎯 Purpose
Tell the interviewer what time/space your plan will achieve — BEFORE writing code.

## 🧠 What interviewer is testing
- That you can predict complexity (not just compute it after)
- That you respect their time — they can stop you if your target is wrong

## 🇬🇧 English phrases

```
"This approach is O(n) time and O(n) space."
"We trade space for time — using extra memory to avoid the n² scan."
"The dominant cost is the sort, which is O(n log n)."
"Auxiliary space is O(k) — only the heap, not counting the output."
```

## 📚 Required knowledge — complexity expression patterns

**Time:**
- *"O(n) because we go through the array once."*
- *"O(n log n) because of the sort."*
- *"O(n × m) where n is rows and m is columns."*
- *"O(2ⁿ) because we explore every subset."*
- *"Amortized O(1) per operation."*

**Space:**
- *"O(n) for the hash map."*
- *"O(1) extra space — we only use a few variables."*
- *"O(h) for the recursion stack, where h is tree height."*
- *"O(V + E) for the graph adjacency list."*

## 🔑 Always distinguish

| Term | Meaning |
|---|---|
| **Total space** | Includes input + output + auxiliary |
| **Auxiliary space** | Only what YOUR algorithm allocates beyond input |
| **Recursion stack** | Counts as space! Often O(log n) for balanced, O(n) for skewed |

## ⚠️ Common mistakes

- Stating complexity AFTER coding, not before → wasted time
- Forgetting recursion stack in space analysis
- Confusing "best case" with "worst case" (interviews care about worst)

## 🔁 Drill

For each plan, state O(time) + O(space) upfront:

1. **Two Sum with hash map** → O(n) time, O(n) space.
2. **Merge two sorted lists** → O(n + m) time, O(1) extra space (in-place pointers).
3. **DFS on a tree to find max depth** → O(n) time, O(h) space (h = tree height).
