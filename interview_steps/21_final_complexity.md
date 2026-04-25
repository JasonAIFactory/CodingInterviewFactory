# Step 21 — Final Complexity (Time + Space + Trade-off)

## 🎯 Purpose
Wrap up with a clean statement of complexity AND a trade-off discussion.

## 🧠 What interviewer is testing
- Big O fluency
- Awareness of trade-offs (most candidates state ONE complexity; seniors discuss alternatives)

## 🇬🇧 English phrases

```
"The time complexity is O(n) because we go through the array once."
"The space complexity is O(n) for the hash map.
 If we ignore the output, the auxiliary space is also O(n)."
"We could reduce space to O(1) by sorting first, but then time becomes O(n log n)."
"Given the input size, this trade-off is the right one."
```

## 📚 Required knowledge — closing template

**Three lines, always:**

1. **Time** — *"O(?), because [reason]."*
2. **Space** — *"O(?), used by [thing]."*
3. **Trade-off** — *"We could also do X, which gives O(?) but requires Y."*

## 🔑 Common alternative trade-offs to mention

| Original | Alternative | Trade-off |
|---|---|---|
| Hash map (O(n) space) | Sort + two pointers | O(1) extra space, O(n log n) time |
| Recursive memoization | Iterative DP table | Same complexity, no stack overflow |
| Heap top-k (O(n log k)) | QuickSelect | O(n) average but O(n²) worst |
| BFS shortest path | Bidirectional BFS | Faster in practice, more memory |
| Standard DP table | Rolling array | Same time, O(1) or O(n) space |

## ⚠️ Common mistakes

- Stating only time, not space
- Saying "O(n)" without saying "because of what"
- Not discussing the trade-off — feels incomplete

## 🔁 Drill

Close each problem with the 3-line template:

1. **Two Sum hash map** →
   - Time: O(n), one pass.
   - Space: O(n) for the map.
   - Trade-off: O(1) space possible by sort + two pointers, but O(n log n) time.

2. **Kth largest with min-heap** →
   - Time: O(n log k).
   - Space: O(k) for the heap.
   - Trade-off: QuickSelect is O(n) average but O(n²) worst case.

3. **DFS max depth on tree** →
   - Time: O(n), each node visited once.
   - Space: O(h) recursion stack.
   - Trade-off: BFS gives same time, O(w) space (w = max width).
