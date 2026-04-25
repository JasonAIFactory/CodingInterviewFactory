# Step 10 — Make Your OWN Small Example

## 🎯 Purpose
After tracing the given example, invent a tiny one yourself.
Catches misunderstandings + signals you're testing your own logic.

## 🧠 What interviewer is testing
Initiative + willingness to verify, not just trust.

## 🇬🇧 English phrases

```
"Let me also try a small example I make up — say nums = [3, 1, 4]."
"What if the input is just [1] — would the expected output be ___?"
"Let me try an edge case — empty input. The expected return would be ___?"
```

## 📚 Required knowledge

**Pick examples that probe ONE thing:**

| Probe goal | Example to use |
|---|---|
| Smallest non-trivial | 2 elements |
| Edge case | empty `[]`, single `[x]` |
| Duplicates | `[3, 3, 3]` |
| Negatives | `[-1, -2, 1]` |
| Sorted descending | `[5, 4, 3, 2, 1]` |
| All same | `[7, 7, 7]` |

**Keep it SMALL. 2–4 elements max. You need to trace it in your head.**

## 🔑 Why this earns points

- Interviewer expects you to trace given example. ✅ baseline
- Inventing your own and tracing it = bonus signal of independent verification
- It often surfaces ambiguity ("oh wait, what if duplicates?")

## ⚠️ Common mistakes

- Picking too complex an example (can't trace it mentally)
- Using same example as the interviewer (no new info)
- Not following up with the trace

## 🔁 Drill

For each problem, invent a 2–3 element edge example + state expected output:

1. **Two Sum** → `[3, 3], target=6` (duplicates) → `[0, 1]`
2. **Longest substring without repeating** → `"aaaa"` → `1`
3. **Reverse linked list** → single node `1 → None` → `1 → None`
