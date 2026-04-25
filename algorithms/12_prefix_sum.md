# Prefix Sum

**O(1) range sum** after O(n) preprocessing.

## 🎯 Essence (memorize this one line)

> *"Add up cumulative sums first. Then any range sum is just subtraction in O of one."*

## 🧠 How it works (principle)

Pre-aggregate cumulative sums so any range can be computed in O(1) by **subtraction**: `sum[l..r] = prefix[r+1] - prefix[l]`. For "subarray sum equals K" patterns, combine with a hash map — for each running prefix `P`, check if `P - K` was seen before. If yes, the elements in between sum to K. Trades O(n) preprocessing for fast queries.

## 🔵 Use when

- Many range sum queries on a fixed array
- "Subarray sum equals K" (with hash map)
- "Continuous subarray with sum / equal balance"

## 💡 Template (basic prefix array)

```python
prefix = [0] * (n + 1)
for i, x in enumerate(arr):
    prefix[i + 1] = prefix[i] + x

# Sum of arr[l..r] inclusive — O(1)
range_sum = prefix[r + 1] - prefix[l]
```

## 💡 Template (subarray sum equals K — running prefix + hash map)

```python
counts = {0: 1}              # prefix sum -> count of occurrences
prefix = 0
result = 0
for num in nums:
    prefix += num
    result += counts.get(prefix - k, 0)
    counts[prefix] = counts.get(prefix, 0) + 1
return result
```

## 💡 Template (2D prefix sum)

```python
prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
for i in range(rows):
    for j in range(cols):
        prefix[i+1][j+1] = matrix[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]

# Sum of submatrix (r1, c1) to (r2, c2) inclusive
total = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
```

## 🇬🇧 What to say

- *"Prefix sum lets me compute any range sum in O of one after O of n preprocessing."*
- *"Combined with a hash map, I can find subarrays summing to K in O of n total."*
- *"For 2D, inclusion-exclusion handles the overlapping rectangle parts."*
