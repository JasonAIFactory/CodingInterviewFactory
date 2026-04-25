# Step 18 — Dry Run with the Given Example

## 🎯 Purpose
Trace your written code with concrete values — out loud — to verify correctness.

## 🧠 What interviewer is testing
Whether your code actually works, before they have to point out a bug.

## 🇬🇧 English phrases

```
"Let me trace through with the given example to verify."
"With nums = [2, 7, 11, 15] and target = 9..."
"At iteration 0: i=0, num=2, complement=7, seen is empty, store seen={2: 0}."
"At iteration 1: i=1, num=7, complement=2, found in seen at index 0,
 return [0, 1]. Correct."
```

## 📚 Required knowledge — dry run technique

**Track variables in a TABLE on the whiteboard / mentally:**

For Two Sum trace:

| i | num | complement | seen (before) | found? | action |
|---|---|---|---|---|---|
| 0 | 2 | 7 | {} | no | store {2: 0} |
| 1 | 7 | 2 | {2: 0} | YES at 0 | return [0, 1] |

**Read out the table row by row.**

## 🔑 What to verify

1. **Loop bounds**: does it run the right number of times?
2. **Index arithmetic**: any off-by-one?
3. **Return value**: matches expected?
4. **State updates**: variables change as expected?

## ⚠️ Common mistakes

- Saying "this looks right" without tracing
- Tracing too fast, jumping over key iterations
- Tracing only the happy path, not the early-return case

## 🔁 Drill

Dry run each:

1. **`is_palindrome("aba")`** — l=0, r=2: 'a'=='a', l=1, r=1, loop exits, return True.
2. **`reverse([1, 2, 3, 4])`** in place — l=0,r=3 swap → [4,2,3,1]; l=1,r=2 swap → [4,3,2,1]; loop exits.
3. **`max_depth(root)`** for `1 -> 2 -> 3 (left chain)`: depth(3)=1, depth(2)=2, depth(1)=3.
