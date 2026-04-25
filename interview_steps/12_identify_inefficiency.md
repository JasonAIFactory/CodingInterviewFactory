# Step 12 — Identify the Inefficiency ⭐

## 🎯 Purpose
Bridge from brute force to optimization by NAMING what's wasteful.
This is the THINKING step — interviewers grade this heavily.

## 🧠 What interviewer is testing
Whether you spot redundancy. This is what separates "I memorized the answer" from "I figured it out."

## 🇬🇧 English phrases

```
"I notice we are doing repeated work."
"We keep computing the same subproblem multiple times."
"We re-scan the same elements in every iteration."
"Each lookup takes O(n), but we do n of them — that's where O(n²) comes from."
"The bottleneck is ___."
```

## 📚 Required knowledge — common forms of waste

| Inefficiency | Optimization that fixes it |
|---|---|
| **Repeated lookups** in array | Hash map for O(1) lookup |
| **Repeated computation** of subproblems | Memoization / DP |
| **Re-scanning the same window** | Sliding window |
| **Re-sorting** within loop | Sort once outside |
| **Linear search in sorted data** | Binary search |
| **Unnecessary full sort** when only top-k needed | Heap of size k |
| **Recursion exploring same path** | Memoization or pruning |
| **Storing whole list** when only running stat needed | Single accumulator |

## 🔑 The script (transition phrase)

> *"In the brute force, **[describe the waste]**.  
> If I can avoid that by **[mechanism]**, I can drop from O(?) to O(?)."*

## ⚠️ Common mistakes

- Jumping to "let me use a hash map" without saying WHY
- Naming the optimization but skipping the waste analysis

## 🔁 Drill

For each brute force, name the inefficiency:

1. **Two Sum nested loop**: re-scanning for the complement — could store seen values in a hash map.
2. **Fibonacci recursion**: recomputing fib(k) many times — could memoize.
3. **Max in every k-window via re-scan**: re-scanning k elements per window — could use monotonic deque.
