# Step 07 — Definition Clarification

## 🎯 Purpose
Pin down the meaning of any FUZZY word in the problem statement.

## 🧠 What interviewer is testing
Whether you assume vs verify. Assuming = junior. Verifying = senior.

## 🇬🇧 English phrases

```
"What does '___' mean exactly in this problem?"
"Could you clarify what counts as a '___'?"
"By '___', do you mean ___ or ___?"
"Just to be sure, is ___ inclusive or exclusive?"
```

## 📚 Required knowledge — common fuzzy terms

| Fuzzy term | Possible meanings — ask! |
|---|---|
| **Substring** | Contiguous slice |
| **Subsequence** | Any subset preserving order (not contiguous) |
| **Subset** | Any subset, order doesn't matter |
| **Adjacent** | Horizontal/vertical only? Or includes diagonal? |
| **Connected** | 4-directional or 8-directional in a grid? |
| **Valid** | What rules define validity? |
| **Palindrome** | Case sensitive? Whitespace counts? |
| **Anagram** | Case sensitive? Spaces count? |
| **Sorted** | Ascending? Descending? Lexicographic for strings? |
| **Distinct** | Different values, or different positions? |
| **Range** | `[a, b]` inclusive both? Or `[a, b)`? |
| **Path** | In a tree/graph: must end at leaf? Can revisit? |
| **Word** | Whitespace-separated? Punctuation handling? |

## 🔑 Specific gotcha pairs

- **"Substring" vs "Subsequence"** — substring is contiguous, subsequence skips allowed
- **"Subset" vs "Permutation"** — subsets ignore order, permutations honor order
- **"Tree" vs "Graph"** — tree has no cycles; graph might
- **"DAG" vs "graph"** — DAG = directed acyclic; topo sort works only on DAG

## ⚠️ Common mistakes

- Assuming "substring" when problem means "subsequence"
- Solving for 4-directional when 8-directional was intended (or vice versa)
- Treating "range [a, b]" as exclusive when inclusive

## 🔁 Drill

For each problem, name a fuzzy word to clarify:

1. **"Longest palindromic substring"** → Case sensitive? Single char counts?
2. **"Word break"** → Word = dictionary entry, or whitespace token?
3. **"Valid Sudoku"** → Each 3x3 box, row, column — all the rules?
