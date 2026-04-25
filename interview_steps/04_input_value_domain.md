# Step 04 — Input Value Domain

## 🎯 Purpose
Find out the *kind* of values inside the input.
Negatives, duplicates, and bounds change which algorithm works.

## 🧠 What interviewer is testing
Whether you anticipate edge cases that BREAK common algorithms.

## 🇬🇧 English phrases

```
"Can the values be negative? Can they be zero?"
"Are there duplicates in the input?"
"Are values bounded? For example, 0 to 100, or arbitrary integers?"
"Are values unique?"
"Are they integers, floats, or could they be very large?"
```

## 📚 Required knowledge — what each domain enables/breaks

| Domain | Algorithm enabled | Algorithm broken |
|---|---|---|
| **All positive** | Sliding window for max sum | — |
| **Has negatives** | Prefix sum + hash map | Naive sliding window for max sum |
| **Bounded range (e.g. 0-100)** | Counting sort O(n+k), bucket sort | — |
| **All unique** | Set is enough | Counter / multiset |
| **Has duplicates** | Need Counter / multiset | Set-based dedup misses count |
| **Float values** | — | Equality comparisons unsafe (use epsilon) |
| **Very large numbers** | Python int is fine; other langs need BigInt | Bit operations may overflow |
| **Only lowercase letters** | Array of size 26 instead of dict | — |

## 🔑 Classic gotchas

1. **Sliding window for "max sum subarray"** assumes positives. If negatives → use Kadane's, not sliding window.
2. **Two-pointer "find pair summing to k"** assumes sorted. Without sort, use hash map.
3. **Counting sort** is O(n+k) — only useful if k (range) is small.

## 🎯 Selectively-asked — by problem type

Only ask these when the problem involves the matching type:

| If problem involves... | Ask... |
|---|---|
| **Integer math** | *"Could the result overflow standard int range? Should I worry?"* |
| **Float values** | *"Should I use an epsilon for equality comparisons?"* |
| **Strings** | *"ASCII only, or Unicode possible? Case-sensitive?"* |
| **Top-K / kth** | *"Could k be larger than n? Could k be 0?"* |
| **Graph** | *"Could the graph be disconnected? Cycles possible? Self-loops?"* |
| **Tree** | *"Could there be duplicate values? Negative values?"* |
| **Linked list** | *"Could the list have a cycle?"* |
| **Numbers** | *"Treat -0 the same as 0? Any special handling for INT_MIN?"* |
| **Date / time** | *"Time zones to handle? Inclusive or exclusive ranges?"* |
| **Currency / money** | *"Use float, or fixed decimal to avoid precision bugs?"* |

> 💡 In Python, integer overflow doesn't happen, but **mention it anyway** —
> it shows you'd catch it in C++/Java. Senior signal.

## ⚠️ Common mistakes

- Coding sliding window without checking for negatives
- Using `set` when duplicates matter (count differs from set size)
- Assuming integers when input is float (`==` is unsafe)

## 🔁 Drill

For each, name what to ask:

1. **"Find longest subarray with sum k"** → Negatives allowed? (changes algorithm)
2. **"Most frequent element"** → Bounded range? (enables counting array)
3. **"Find duplicates"** → Are duplicates guaranteed to exist? Single or multiple?
