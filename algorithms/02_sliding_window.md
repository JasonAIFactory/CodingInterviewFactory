# Sliding Window

**O(n) total** — each element visited at most twice.

## 🎯 Essence (memorize this one line)

> *"Slide a window through the array. Add right, drop left. Each element visited at most twice."*

## 🧠 How it works (principle)

Avoid re-scanning by SLIDING the window — add one element on the right, drop one on the left. Each element enters and leaves the window at most once → O(n) total. The key insight: instead of testing every substring (O(n²)), maintain a running view and update incrementally as it moves. Works for "contiguous subarray with constraint" problems.

## 🔵 Use when

- "Longest / shortest / max / min substring with constraint"
- Subarray with sum / unique / k distinct
- Permutation in string, anagram in string

## 💡 Two flavors

- **Fixed window** (size k): slide right, drop left
- **Variable window**: expand right, shrink left when constraint breaks

## 💡 Template (variable window)

```python
last_seen: dict[str, int] = {}
left = 0
best = 0
for right, ch in enumerate(s):
    if ch in last_seen and last_seen[ch] >= left:
        left = last_seen[ch] + 1
    last_seen[ch] = right
    best = max(best, right - left + 1)
```

## 💡 Template (fixed window, sum)

```python
window_sum = sum(nums[:k])
best = window_sum
for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
    best = max(best, window_sum)
```

## 🇬🇧 What to say

- *"Sliding window — O of n total, each element visited at most twice."*
- *"Right always moves forward. Left jumps when the constraint breaks."*
- *"I use a hash map to track the latest position of each element."*
