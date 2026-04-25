# Linked List

**O(1) insert/delete given a node reference.** O(n) to find.

## 🎯 Essence (memorize this one line)

> *"O of one insert and delete given a node. O of n to find. Doubly linked for free reverse traversal."*

## ✅ Pros / ❌ Cons

- ✅ O(1) insert/delete given a reference
- ✅ Dynamic size, no resize cost
- ❌ O(n) random access
- ❌ Cache-unfriendly

## 🔵 Use when

- LRU Cache (combined with hash map)
- Build queue / stack from scratch
- O(1) insert when position is known

## 💡 Trade-off (vs Array)

- Linked list: O(n) access, O(1) insert with reference
- Array: O(1) access, O(n) middle insert
- Doubly linked needed for O(1) middle removal

## 🇬🇧 What to say

- *"Doubly linked list gives O of one removal given a node reference."*
- *"Hash map plus doubly linked list is the LRU pattern."*
- *"Sentinel head and tail nodes avoid null checks at boundaries."*
