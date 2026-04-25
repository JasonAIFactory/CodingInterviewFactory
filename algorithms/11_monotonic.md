# Monotonic Stack / Deque

**O(n) total** — stack/deque maintains increasing or decreasing order.

## 🎯 Essence (memorize this one line)

> *"Stack stays in order. Pop useless elements when a new one breaks the order. O of n total."*

## 🧠 How it works (principle)

Maintain a stack/deque where stored values are in strictly increasing or decreasing order. When a new element BREAKS that order, POP elements that are now "useless" — they can never be the answer for any future query. Each element is pushed and popped at most ONCE → total work is O(n), not O(n²).

> 💡 **Key insight**: if element X is smaller than incoming Y, and we're looking for "next greater," X is OBSOLETE for everyone after Y — Y dominates it. So X gets popped without regret.

## 🔵 Use when

- "Next greater / smaller element"
- Daily Temperatures, Largest Rectangle in Histogram
- Sliding window max/min

## 💡 Template (next greater — monotonic decreasing stack)

```python
result = [-1] * n
stack = []                          # indices, values monotonically decreasing
for i, num in enumerate(nums):
    while stack and nums[stack[-1]] < num:
        result[stack.pop()] = num
    stack.append(i)
```

## 💡 Template (sliding window max — monotonic decreasing deque)

```python
from collections import deque

dq = deque()                        # indices
result = []
for i, num in enumerate(nums):
    while dq and dq[0] <= i - k:
        dq.popleft()                # out of window
    while dq and nums[dq[-1]] < num:
        dq.pop()                    # smaller, useless
    dq.append(i)
    if i >= k - 1:
        result.append(nums[dq[0]])
```

## 🇬🇧 What to say

- *"Monotonic stack maintains decreasing values — when I see a larger one, I pop and record the answer."*
- *"Each element is pushed and popped at most once, so total is O of n."*
- *"For sliding window max, the front of the deque is always the current max."*
