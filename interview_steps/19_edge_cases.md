# Step 19 — Proactively Name Edge Cases

## 🎯 Purpose
List edge cases YOURSELF, before the interviewer asks.
Each one named = points earned.

## 🧠 What interviewer is testing
Defensive thinking. Whether you anticipate failure modes.

## 🇬🇧 English phrases

```
"Let me think about edge cases:"
"  - Empty input — returns ___."
"  - Single element — returns ___."
"  - All duplicates — works because ___."
"  - Maximum size — still O(n), so it scales."
"  - No valid answer exists — returns ___."
```

## 📚 Required knowledge — universal edge case checklist by data type

### Arrays / lists

- [ ] Empty `[]`
- [ ] Single element `[x]`
- [ ] Two elements (often the smallest non-trivial)
- [ ] All same elements `[3, 3, 3]`
- [ ] Sorted ascending / descending
- [ ] Negatives / zero
- [ ] Maximum size — does it scale?
- [ ] Duplicates of the answer

### Strings

- [ ] Empty `""`
- [ ] Single char `"a"`
- [ ] Whitespace-only `"   "`
- [ ] Mixed case
- [ ] Unicode / special chars
- [ ] Numerical chars only

### Trees

- [ ] Null root
- [ ] Single node
- [ ] Skewed tree (looks like linked list)
- [ ] Balanced
- [ ] Duplicates allowed?
- [ ] Negative values

### Graphs

- [ ] Empty graph
- [ ] Single node
- [ ] Disconnected components
- [ ] Cycle present
- [ ] Self-loop
- [ ] Parallel edges

### Linked lists

- [ ] Empty list (head=None)
- [ ] Single node
- [ ] Two nodes
- [ ] Cycle
- [ ] Operating on head (special)
- [ ] Operating on tail (special)

### Numerical

- [ ] Zero
- [ ] Negative
- [ ] Maximum int (overflow in other langs)
- [ ] One

## 🔑 The trick — say it out loud, even if your code already handles it

> ✅ *"Empty input — my early return handles this, returns []."*
> ❌ Say nothing about it.

The point is **demonstrating you THOUGHT about it**.

## 🎯 Special concerns by problem domain

Domain-specific edge cases that go BEYOND the universal checklist:

| Problem domain | Extra edge cases to mention |
|---|---|
| **Integer math** | Overflow, underflow, division by zero, negative zero, `abs(INT_MIN)` trap |
| **Floating point** | NaN, infinity, -0.0 vs 0.0, equality with epsilon |
| **String parsing** | Leading/trailing whitespace, multiple consecutive spaces, mixed case, Unicode chars, empty after trim |
| **Top-K / kth** | k = 0, k > n, k = 1, ties at the boundary |
| **Graph** | Self-loop, parallel edges, disconnected components, cycle, single-node graph, no edges at all |
| **Linked list** | Cycle, single node, head removal, tail removal, head == tail |
| **Tree** | Skewed (linked-list shape), duplicate values, single node, null root, all left or all right children |
| **Sliding window** | Window > array length, window = 0, all same elements, window = entire array |
| **Binary search** | Target outside range (smaller / larger than all), duplicates of target, empty array, array of size 1 |
| **Recursion** | Stack depth on skewed input, base case never hit, infinite recursion risk |
| **Sorting** | Already sorted, reverse sorted, all equal, single element, two elements |
| **Hash map / set** | Hash collision in custom keys, mutating keys (don't!), `None` as key |
| **2D grid** | Empty grid, single row, single column, 1x1, jagged rows |
| **Bit operations** | Negative numbers (sign bit!), zero, all bits set |

> 💡 Pick 2–3 from the relevant domain. Don't recite all — that's annoying.

## ⚠️ Common mistakes

- Skipping the edge case enumeration
- Only noticing edges after interviewer says "what about empty?"
- Listing edges but not stating the EXPECTED behavior

## 🔁 Drill

For each problem, list 3 edge cases + behavior:

1. **Two Sum** → `[]` returns `[]`; `[3, 3]` target 6 returns `[0, 1]`; no pair returns `[]`.
2. **Reverse linked list** → empty (None) returns None; single node returns same node; two nodes swap.
3. **Number of islands in grid** → empty grid 0; all water 0; all land 1; 1x1 with land 1.
