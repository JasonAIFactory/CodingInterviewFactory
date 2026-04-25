# Heap / Top-K Pattern

**O(n log K)** to find top K with a min-heap of size K.

## 🎯 Essence (memorize this one line)

> *"Min-heap of size K. New element pushes out the smallest. End up with the K largest."*

## 🧠 How it works (principle)

A heap maintains the smallest (or largest) element at the top in O(1), at the cost of O(log n) insert/remove. **For top K largest**: keep a MIN-heap of size K. When full, only elements LARGER than the heap's smallest get to push out the current smallest. After processing all n elements, the heap contains exactly the K largest. Same idea reversed for top K smallest (use max-heap or negate values).

> 💡 **Why min-heap for top-K largest** (counterintuitive): we constantly compare new elements against the SMALLEST in our K-set; if new is larger, it deserves to replace the smallest.

## 🔵 Use when

- "Top K largest / smallest"
- "K closest points"
- "K most frequent elements"
- Streaming data — running stats

## 💡 Template (top K largest)

```python
import heapq

heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)         # remove smallest
return heap   # K largest, in arbitrary order
```

## 💡 Template (K closest points — sort by distance)

```python
heap = []
for x, y in points:
    dist = x * x + y * y
    heapq.heappush(heap, (dist, [x, y]))
return [heapq.heappop(heap)[1] for _ in range(k)]
```

## 💡 Template (K most frequent)

```python
from collections import Counter
counts = Counter(nums)
return heapq.nlargest(k, counts.keys(), key=counts.get)
```

## 🇬🇧 What to say

- *"Min-heap of size K gives top K in O of n log K."*
- *"Better than full sort O of n log n when K is much smaller than n."*
- *"For tuples, heap sorts by the first element — useful for distance + point pairs."*
