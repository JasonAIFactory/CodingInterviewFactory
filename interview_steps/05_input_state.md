# Step 05 — Input State

## 🎯 Purpose
Discover the *condition* of the input — sorted, empty, valid?

## 🧠 What interviewer is testing
Whether you exploit pre-existing structure (like sortedness) and whether you handle missing input.

## 🇬🇧 English phrases

```
"Is the input sorted? In what order?"
"Can the input be empty?"
"Can the input be null?"
"Can I assume the input is always valid?"
"Is whitespace meaningful? Is the input case-sensitive?"
"Is the input mutable, or do I need to preserve it?"
```

## 📚 Required knowledge

| Input state | Unlocks / requires |
|---|---|
| **Already sorted** | Binary search O(log n), two pointers O(n) |
| **Almost sorted (k off)** | Insertion sort O(nk), heap of size k |
| **Empty allowed** | Always handle: `if not nums: return ...` |
| **Null possible** | Handle: `if nums is None: ...` |
| **Invalid possible** | Need validation block |
| **Mutable** | Can sort in place |
| **Immutable required** | Make a copy before modifying |
| **Streaming (one pass)** | No backtracking; use online algos |

## 🔑 Default empty/null returns

| Output type | Empty input return |
|---|---|
| List | `[]` |
| String | `""` |
| Number / count | `0` |
| Boolean | usually `True` (vacuous truth) or False — ask! |
| Tree node | `None` |

## 🎯 Selectively-asked — by problem type

Only ask these when the problem involves the matching type:

| If problem involves... | Ask... |
|---|---|
| **String parsing** | *"Is whitespace meaningful? Should I trim leading/trailing?"* |
| **String matching** | *"Is matching case-sensitive?"* |
| **Array transform** | *"Can I mutate in place, or must I preserve the input?"* |
| **Large data** | *"Does the data fit in memory, or is it streaming?"* |
| **2D grid** | *"Are all rows the same length?"* |
| **Sorted input** | *"Sorted by what — value, lexicographic, custom key?"* |
| **Database / file** | *"Could the input have duplicates from upstream?"* |
| **Time-series** | *"Sorted by timestamp? Any gaps?"* |

## ⚠️ Common mistakes

- Forgetting empty check at line 1 of function
- Sorting an "already sorted" input (wasted O(n log n))
- Mutating input when it should be preserved

## 🔁 Drill

For each, what state question to ask?

1. **"Find median of two sorted arrays"** → Already sorted? Same length?
2. **"Print all permutations"** → Can input contain duplicates?
3. **"Reverse a string"** → In place or new string? (Python: strings immutable, must return new)
