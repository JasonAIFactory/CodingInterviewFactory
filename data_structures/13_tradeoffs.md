# Trade-off Phrases — for Step 18 (Final Complexity)

When the interviewer asks *"Could you do this differently?"* — say one of these.

## Hash Map vs Sort + Two Pointers

> *"Hash map is O of n time and O of n space. Sort plus two pointers is O of n log n time and O of one extra space. I'll pick hash map since memory isn't tight."*

## Heap vs Sort (Top K)

> *"Heap of size K is O of n log K — better than sorting O of n log n when K is small. Also works for streaming."*

## BFS vs DFS

> *"BFS gives shortest path in unweighted graphs. DFS is better for finding all paths or for tree traversal."*

## Recursion vs Iteration

> *"Recursion is cleaner for trees. For very deep input I'd switch to iteration with an explicit stack to avoid stack overflow."*

## Memoization (top-down) vs Tabulation (bottom-up) DP

> *"Top-down with memoization is easier to write. Bottom-up is faster and avoids recursion stack, but requires figuring out the iteration order."*

## Hash Map vs BST

> *"Hash map is O of one but unordered. BST is O of log n but supports sorted iteration and range queries."*

## Linked List vs Array

> *"Linked list excels at insertions given a node reference. Array excels at random access. Array is the safer default."*

## In-place vs New Allocation

> *"In-place saves memory but mutates input. I'd ask if the caller needs the original preserved."*

## Counting Sort vs Comparison Sort

> *"If the value range is small, counting sort is O of n plus k — beats O of n log n. For arbitrary integers, stick with comparison sort."*

---

## 🎯 Universal closing phrase

> *"There are a few trade-offs we could discuss — would you like me to compare alternatives?"*

→ Always offer this at the end of Step 18. Bonus signal.
