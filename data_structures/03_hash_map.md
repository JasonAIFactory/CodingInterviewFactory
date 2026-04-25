# Hash Map (`dict`)

**O(1) get/set/delete** average.

## 🎯 Essence (memorize this one line)

> *"Key to value lookup in O of one. Trade space for time. Keys must be hashable."*

## ✅ Pros / ❌ Cons

- ✅ O(1) lookup, insert, delete
- ✅ Flexible keys (anything hashable)
- ❌ Extra memory overhead
- ❌ No sorted order

## 🔵 Use when

- Find pair / complement (Two Sum)
- Count frequency (`Counter`)
- Group by key (`defaultdict`)
- Cache / memoization

## 💡 Trade-off (vs Sort + Two Pointers)

- Hash map: O(n) time, O(n) space
- Sort + 2P: O(n log n) time, O(1) extra space
- Pick hash map when memory isn't constrained

## 🇬🇧 What to say

- *"I'll use a hash map — O of one lookup."*
- *"We trade space for time."*
- *"Keys must be hashable — strings, tuples, ints."*
