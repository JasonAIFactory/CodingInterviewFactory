# Step 20 — Off-By-One Boundary Check

## 🎯 Purpose
Verify that loop bounds, indices, and conditions are correct at the BOUNDARIES.
Off-by-one is the #1 silent bug.

## 🧠 What interviewer is testing
Attention to detail. Whether you proactively check edges, or wait for failure.

## 🇬🇧 English phrases

```
"Let me check the boundary conditions."
"Does this work at i = 0?"
"Does this work at i = n - 1?"
"Is the loop inclusive or exclusive of the upper bound?"
"What if low equals high — does the loop run zero times or once?"
```

## 📚 Required knowledge — common off-by-one traps

### Range / loop bounds

| Code | Iterates over |
|---|---|
| `range(n)` | `0` to `n-1` |
| `range(1, n)` | `1` to `n-1` |
| `range(n + 1)` | `0` to `n` (inclusive) |
| `for i, x in enumerate(arr)` | `i = 0` to `len(arr) - 1` |

### Slicing

| Code | Includes |
|---|---|
| `arr[0:k]` | indices 0 to k-1 (length k) |
| `arr[:k]` | same as above |
| `arr[-1]` | last element |
| `arr[-k:]` | last k elements |

### Two pointers / sliding window

- `while l < r:` runs while pointers haven't crossed
- `while l <= r:` runs ONE more time when l == r
- For binary search, choosing `<` vs `<=` is the classic bug

### Binary search bounds

```python
# Standard:  while lo < hi:
# - lo + 1 = ... when adjusting
# - returns lo (the insertion point)

# Inclusive:  while lo <= hi:
# - careful when narrowing — can infinite loop
```

### Window length

- Window from `i` to `j` inclusive has length `j - i + 1` (NOT `j - i`)

## 🔑 Quick boundary tests

For any loop, ask:
1. What happens when input is empty? Loop runs 0 times — is that OK?
2. What happens when input is 1 element? Loop runs 1 time — is the result right?
3. What happens at the LAST iteration? Any out-of-bounds index?

## ⚠️ Common mistakes

- `range(n)` when meaning to include `n`
- `arr[i + 1]` at `i = n - 1` → IndexError
- Window length: `j - i` instead of `j - i + 1`
- Binary search: never updating `lo` or `hi` → infinite loop

## 🔁 Drill

Find the off-by-one:

1. `for i in range(len(arr)): if arr[i] == arr[i + 1]:` → fails at i = n-1.  
   **Fix**: `range(len(arr) - 1)`.

2. `mid = (lo + hi) // 2; if arr[mid] < target: lo = mid` → infinite loop.  
   **Fix**: `lo = mid + 1`.

3. Window `[i, j]` has length `j - i`. → wrong.  
   **Fix**: `j - i + 1`.
