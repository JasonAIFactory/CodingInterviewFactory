# Step 06 — Output Format

## 🎯 Purpose
Know exactly WHAT and in WHAT FORMAT to return.
Wrong return type = automatic fail even if logic is right.

## 🧠 What interviewer is testing
Attention to interface contract.

## 🇬🇧 English phrases

```
"What should I return — the value, the index, the count, or a boolean?"
"If multiple valid answers exist, should I return any one, or all of them?"
"Should I return indices or the actual values?"
"Should I modify in-place, or return a new structure?"
"What is the expected output format — list, set, string, integer?"
"What should I return if no valid answer exists? Empty? -1? Null?"
```

## 📚 Required knowledge

**Most common output traps:**

| Problem-type pattern | Could be... |
|---|---|
| "Find the pair" | Indices `[i, j]` OR values `[a, b]` |
| "Reverse the list" | New list returned OR mutate in place returning None |
| "Find ALL solutions" | List of lists |
| "Find ANY one solution" | Single list |
| "Count" | Just the integer |
| "Exists?" | Boolean |
| "Smallest/largest" | The value, not the index — or both? |

## 🔑 No-answer return conventions (always ASK)

| Common returns when no answer | Used for |
|---|---|
| `[]` | Lists of pairs/groups |
| `-1` | Index lookups (LeetCode standard) |
| `None` | Tree/linked list nodes |
| `0` | Count problems |
| `False` | Boolean problems |
| `""` | String search |

## 🎯 Selectively-asked — by problem type

Only ask these when the problem involves the matching type:

| If problem involves... | Ask... |
|---|---|
| **Listing all results** | *"Does output ordering matter? Sorted? Lexicographic?"* |
| **Sorting** | *"Should sort be stable — preserve relative order of equal elements?"* |
| **Pairs / triples** | *"Is there a canonical order within each tuple? e.g., [smaller, larger]?"* |
| **Grouping** | *"Should groups be sorted? By size? By first element?"* |
| **Tree / Graph** | *"Return as list, or rebuild a new tree/graph?"* |
| **Counts** | *"Return total count, or counts per category?"* |
| **Strings** | *"Lowercase the result? Strip whitespace?"* |
| **Floats** | *"Round to a specific precision?"* |

## ⚠️ Common mistakes

- Returning value when problem wants index (or vice versa)
- Returning new list when problem wants in-place mutation
- Returning `None` when problem wants `-1`
- Confusing "all solutions" vs "any one solution"

## 🔁 Drill

For each, name 2 things to clarify about output:

1. **"Two Sum"** → Indices or values? Sorted result or any order?
2. **"Generate all subsets"** → Sorted output? Empty subset included?
3. **"Find first non-repeating character"** → Index or character? `-1` or `None` if none?
