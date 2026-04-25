# Greedy

**Often O(n) or O(n log n).** Local optimal choice → global optimum.

## 🎯 Essence (memorize this one line)

> *"Pick the locally best choice each step. Works only if local choice can't hurt the global answer."*

## 🧠 How it works (principle)

Make the **locally** optimal choice at each step, hoping it leads to **globally** optimal. Works only when the problem has the **greedy-choice property**: a local optimum is guaranteed to be part of some global optimum (provable by exchange argument). When unsure, fall back to DP — DP always works for optimization, but greedy is faster when applicable.

> 💡 **Risk**: greedy without proof can give wrong answers. Always justify why local choice can't hurt the global answer.

## 🔵 Use when

- "Min / max number of X to do Y"
- Interval scheduling
- Task assignment, gas station, jump game
- Partition Labels, Task Scheduler

## 💡 Common patterns

- Sort by some key, then iterate
- Use heap to always pick the best
- Track running state (e.g., max reachable index)

## 💡 Template (interval scheduling — max non-overlapping)

```python
intervals.sort(key=lambda x: x[1])      # sort by END time
count = 0
end = float("-inf")
for start, finish in intervals:
    if start >= end:
        count += 1
        end = finish
return count
```

## 💡 Template (jump game — max reach)

```python
max_reach = 0
for i, jump in enumerate(nums):
    if i > max_reach:
        return False                    # unreachable
    max_reach = max(max_reach, i + jump)
return True
```

## 🇬🇧 What to say

- *"Greedy works here because the local optimal choice leads to the global optimum."*
- *"I sort by ___ and iterate, making the locally best choice each step."*
- *"Greedy needs justification — I should think why local choices won't break global optimality."*
