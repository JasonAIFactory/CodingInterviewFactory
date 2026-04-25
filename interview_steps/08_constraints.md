# Step 08 — Non-Functional Constraints

## 🎯 Purpose
Discover memory limits, query frequency, time priorities — all non-input things that change design.

## 🧠 What interviewer is testing
Awareness that real systems have constraints beyond just the input.

## 🇬🇧 English phrases

```
"Are there memory constraints I should be aware of?"
"Should I optimize for time or for space?"
"Will this be called once, or many times?"
"Is this a real-time / streaming scenario?"
"Can the input fit in memory?"
"Is there a latency requirement per query?"
```

## 📚 Required knowledge — what each constraint implies

| Constraint signal | Approach hint |
|---|---|
| **"Many queries"** (1M lookups) | Preprocess once, cache, build index |
| **"One-time call"** | Direct compute, don't bother indexing |
| **"Memory-tight"** | In-place ops, O(1) extra space, generators |
| **"Real-time / latency"** | O(1) or O(log n) per query, no full scan |
| **"Streaming / can't store"** | Online algorithm, reservoir sampling, running stats |
| **"Distributed / huge data"** | MapReduce-style, external sort |
| **"Read-heavy, write-rare"** | Cache aggressively |

## 🔑 Quick examples

- "Find median of a stream" → can't sort, use 2 heaps (online)
- "Top-k elements with billions of inputs" → external sort or distributed count-min
- "Many queries on a fixed string" → suffix array preprocessing

## 🎯 Selectively-asked — by problem type

Only ask these when the problem involves the matching type:

| If problem involves... | Ask... |
|---|---|
| **Design / shared state** | *"Called from multiple threads? Need thread safety?"* |
| **API / service** | *"What's the latency budget per call? P99?"* |
| **Cache / database** | *"How big is the dataset? Fit in RAM?"* |
| **Distributed scenario** | *"Single node or distributed? Eventual consistency OK?"* |
| **File I/O** | *"Files small enough to load fully, or stream?"* |
| **Real-time** | *"Updates per second? Read vs write ratio?"* |
| **Mobile / embedded** | *"Memory budget tight? Battery / CPU concerns?"* |
| **Search / recommendation** | *"Approximate result OK, or must be exact?"* |

## ⚠️ Common mistakes

- Asking only about input, never about query patterns
- Designing a single-call algorithm when problem implies repeated queries

## 🔁 Drill

For each, what constraint question to ask?

1. **"Auto-complete suggestions"** → How many queries per second? Pre-build trie or compute live?
2. **"Find stock peaks"** → Streaming data or batch? Memory budget?
3. **"Friend recommendations"** → How often does the friend graph change? Precompute or recompute?
