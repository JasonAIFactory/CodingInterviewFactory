# Binary Search

**O(log n)** — sorted input or "search the answer" problems.

## 🎯 Essence (memorize this one line)

> *"Cut the search space in half each step. Needs sorted data or a monotonic answer."*

## 🧠 How it works (principle)

Halve the search space each step using a comparison. Works on (1) sorted data — `arr[mid]` tells you to discard left or right half, OR (2) a monotonic predicate — *"feasible at X means feasible at all X' > X"* (or vice versa). Achieves O(log n) because n / 2 / 2 / 2... reaches 1 in log₂(n) steps. **Critical**: the discard direction must be PROVABLY correct, otherwise you miss the answer.

## 🔵 Use when

- Sorted array + find value
- "Find leftmost / rightmost occurrence"
- "Minimize / maximize X such that condition holds" — binary search on answer
- Koko Bananas, Capacity to Ship Packages, Median of Two Sorted Arrays

## 💡 Template (canonical)

```python
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
return -1
```

## 💡 Template (binary search on answer)

```python
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid          # try smaller
    else:
        lo = mid + 1      # need bigger
return lo
```

## 🇬🇧 What to say

- *"Binary search on a sorted array — O of log n."*
- *"I can also binary search on the answer when the problem is monotonic — feasible at higher values means feasible at all higher values."*
- *"Watch the boundary — `lo = mid + 1` to avoid infinite loops."*
