# Two Pointers

**O(n) time, O(1) extra space.** Two indices walking through a structure based on a comparison.

## 🎯 Essence (memorize this one line)

> *"Two pointers walk through a sorted or paired structure. Each move shrinks the search. O of n with no extra space."*

## 🧠 How it works (principle)

When the structure has order (sorted) or symmetry (palindrome) or pairs (linked list cycle), comparing two positions tells you which side to discard. Each move shrinks the search space by at least one — so total iterations are O(n), not O(n²). Works because each step makes provable progress.

## 🔵 Use when

- Sorted array + find pair / triplet
- Palindrome check
- Cycle detection in linked list (fast & slow)
- Remove duplicates in place

## 💡 Three flavors

- **Opposite ends**: `l = 0, r = n-1`, move toward each other
- **Same direction**: slow + fast, both forward
- **Fast & slow**: cycle detection (Floyd's)

## 💡 Template (opposite ends)

```python
left, right = 0, len(nums) - 1
while left < right:
    s = nums[left] + nums[right]
    if s == target:
        return [left, right]
    elif s < target:
        left += 1
    else:
        right -= 1
```

## 🇬🇧 What to say

- *"Two pointers works because the array is sorted — I move left or right based on the comparison."*
- *"It's O of n with O of one extra space — better than hash map when memory is tight."*
- *"For cycle detection in linked list, I use fast and slow pointers — Floyd's algorithm."*
