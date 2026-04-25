# Step 22 — Follow-up & Scaling Extensions

## 🎯 Purpose
Show you think beyond the immediate problem — toward production realities.

## 🧠 What interviewer is testing
- Big-picture thinking
- Whether you're SDE I (solves the problem) or SDE II (thinks about scale)

## 🇬🇧 English phrases

```
"If the input were too large to fit in memory, I would use a streaming approach."
"If we had to handle multiple queries, I would precompute and cache the result."
"If this were a real-time stream, I would maintain a running statistic."
"If we needed concurrent access, I would add locking around the cache."
"Would you like me to extend this for any of these scenarios?"
```

## 📚 Required knowledge — common follow-up axes

| If interviewer asks... | Mention... |
|---|---|
| "What if input doesn't fit in memory?" | Streaming, external sort, MapReduce, generators |
| "What if many queries?" | Precompute, cache, build an index (trie, segment tree) |
| "What if real-time stream?" | Online algorithms (running mean, reservoir sample, two-heap median) |
| "What about concurrency?" | Locks, copy-on-write, partitioning |
| "What if data is distributed?" | Consistent hashing, MapReduce |
| "What if input is mostly the same?" | Memoization / cache |
| "What if we want top-k continuously?" | Min-heap of size k, updated as data flows |
| "What if very large k?" | Approximation (count-min sketch, HyperLogLog) |

## 🔑 The script

> *"This solves it for the given input. If we scale to **[scenario]**, I would change to **[approach]** because **[reason]**."*

Then OPEN the door:
> *"Would you like to explore that variation?"*

## ⚠️ Common mistakes

- Skipping this entirely — seems "done" but you missed an easy win
- Naming a follow-up but not justifying it
- Going too deep without checking if interviewer wants to explore

## 🔁 Drill

For each problem, propose 1 follow-up:

1. **Two Sum** → "If we had millions of queries on the same array, I'd precompute pair sums into a lookup table."
2. **LRU Cache** → "If multi-threaded, I'd add a lock around get/put, or use a thread-safe variant."
3. **Find median in stream** → "If memory-bound, we could use approximate quantile sketches."
