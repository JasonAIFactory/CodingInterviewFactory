# 🎯 The Amazon Interview Template (Master Checklist)

This is **THE** template. Every problem follows this. No exceptions. No improvising.

> ⚠️ **Mindset first**: This is an INTERVIEW, not a coding contest.
> They score *how you think and communicate*, not just whether the code passes.
> Silence is the #1 killer. Verbalize everything.

---

## 🟦 PHASE 1 — CLARIFY (3–5 min)

> The most undervalued phase. Most candidates lose points HERE before writing a single line.
> Your goal: never assume anything. Ask everything. Repeat the problem back in your own words.

### ✅ Always-Ask Checklist

For EVERY problem, check off ALL of these:

#### 1.1 Restate the problem (always start here)
```
"Let me make sure I understand the problem correctly.
 We are given ___, and we need to return ___. Is that right?"
```
**Why interviewer cares:** Confirms you're solving the *right* problem.

#### 1.2 Input type & structure
```
"What is the input type? Is it a list, a string, a tree, or a graph?"
"If it's a graph, is it represented as adjacency list, matrix, or edge list?"
```
**Why:** Wrong assumption here means wrong solution.

#### 1.3 Input size (CRITICAL — drives complexity choice)
```
"What is the maximum size of n?"
```
**Cheat sheet — what n tells you:**

| n size | Acceptable complexity |
|---|---|
| n ≤ 12 | O(n!) backtracking is fine |
| n ≤ 25 | O(2ⁿ) bitmask / brute force |
| n ≤ 100 | O(n³) is fine |
| n ≤ 5,000 | O(n²) is fine |
| n ≤ 10⁶ | Must be O(n log n) or O(n) |
| n ≤ 10⁹ | Must be O(log n) or O(1) |

#### 1.4 Input value domain
```
"Can values be negative? Can they be zero?"
"Are there duplicates?"
"Are values bounded? For example, 0 to 100, or arbitrary integers?"
"Are values unique?"
```
**Why:** Negatives break some algorithms (sliding window). Bounds enable bucket/counting sort. Duplicates change return type.

#### 1.5 Input state
```
"Is the input sorted?"
"Can the input be empty?"
"Can the input be null?"
"Is whitespace meaningful? Is the input case-sensitive?"
"Can I assume the input is always valid?"
```
**Why:** Sorted unlocks binary search. Empty/null input is the #1 missed edge case.

#### 1.6 Output format
```
"What should I return — the value, the index, the count, or a boolean?"
"If multiple answers exist, return any one, or all?"
"Should I modify in-place, or return a new structure?"
"What is the expected format — list, set, string?"
```
**Why:** Wrong return type = automatic fail.

#### 1.7 Definition clarification
For ANY fuzzy word in the problem:
```
"What does '___' mean exactly in this problem?"
```
Examples:
- "What counts as a *valid* parenthesis sequence?"
- "Does a single character count as a *palindrome*?"
- "Are *substrings* contiguous, or can they skip characters?"
- "Does *adjacent* mean horizontally/vertically only, or also diagonally?"

**Why:** You shows you don't assume — you check.

#### 1.8 Constraints / non-functional
```
"Are there memory constraints I should be aware of?"
"Should I optimize for time or for space?"
"Will this be called once, or many times?"
```
**Why:** A "many times" answer hints at preprocessing or caching.

#### 1.9 Walk through TWO examples (always)
```
"Let me walk through the given example to confirm my understanding."
"Let me also make up a tiny one — say nums = [1, 2, 3]. The expected output would be ___?"
```
**Why:** Catches misunderstandings BEFORE you waste 20 min coding the wrong thing.

---

## 🟦 PHASE 2 — PLAN (3–5 min)

### ✅ Always-Do Checklist

#### 2.1 State the brute force FIRST
Even if you know the optimal:
```
"My first thought is brute force.
 For each element, I would check every other element.
 That gives us O(n²) time and O(1) space."
```
**Why:** Shows you can find *any* solution before optimizing.

#### 2.2 Identify the inefficiency
```
"I notice we are doing repeated work —
 we keep checking the same pairs / recomputing the same subproblems."
```
**Why:** This is the *thinking* they evaluate.

#### 2.3 Propose optimization with data structure justified
```
"If I use a hash map to remember what I've seen,
 I can do the lookup in O(1) instead of O(n)."
```
**Why:** "Why this data structure" matters more than naming it.

#### 2.4 State complexity BEFORE coding
```
"This approach is O(n) time and O(n) space.
 We trade space for time."
```

#### 2.5 Get buy-in
```
"Does this approach sound good before I start coding?"
```
**Why:** If they push back, you save 20 minutes of wrong direction.

---

## 🟦 PHASE 3 — CODE (15–20 min)

### ✅ Always-Do Checklist

#### 3.1 Talk while typing
Never silent. Narrate every block:
```
"I create an empty hash map called seen."
"I loop through the array with enumerate so I have both index and value."
"For each number, I compute the complement and check the map."
```

#### 3.2 Use type hints (Production-level signal)
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    ...
```
**Why:** Reads as senior engineer, not student.

#### 3.3 Validate boundaries
```python
if not nums:
    return []
if k <= 0:
    raise ValueError("k must be positive")
```

#### 3.4 Use helper methods (separation of concerns)
If logic gets long → extract:
```python
def _is_valid(...): ...
def _normalize(...): ...
```
**Why:** Round 2 (Logical & Maintainable) directly grades this.

#### 3.5 No magic numbers / hardcoded values
```python
ALPHABET_SIZE = 26   # ✅
counts = [0] * 26     # ❌ what is 26?
```

#### 3.6 Use early returns (guard clauses)
```python
# ✅ Clean
if not node:
    return 0
return ...

# ❌ Nested
if node:
    return ...
else:
    return 0
```

---

## 🟦 PHASE 4 — TEST (3–5 min)

### ✅ Always-Check Checklist

#### 4.1 Trace the given example
```
"Let me run through with nums=[2,7,11,15], target=9..."
```
**Trace step by step. Don't just say 'it works'.**

#### 4.2 Edge cases — name them out loud (interviewer is grading this)
For ANY problem, always check:

- [ ] **Empty input** — `[]`, `""`, `None`
- [ ] **Single element** — `[x]`, `"a"`
- [ ] **Two elements** — minimum non-trivial
- [ ] **All same elements** — `[3, 3, 3]`
- [ ] **Already sorted / reverse sorted** (if order matters)
- [ ] **Negatives / zero** (if values matter)
- [ ] **Duplicates** (if uniqueness matters)
- [ ] **Maximum size** — does it scale?
- [ ] **No valid answer exists** — what do you return?
- [ ] **Multiple valid answers** — which do you return?

For trees:
- [ ] Single node
- [ ] Skewed tree (looks like a linked list)
- [ ] Balanced vs unbalanced

For graphs:
- [ ] Disconnected components
- [ ] Cycle
- [ ] Self-loop
- [ ] Single node

For strings:
- [ ] Empty string vs single space
- [ ] Case sensitivity
- [ ] Unicode / special chars

#### 4.3 Off-by-one boundary check
```
"Let me check the index boundaries — does this work at i=0 and i=n-1?"
```

---

## 🟦 PHASE 5 — COMPLEXITY (1–2 min)

### ✅ Always-State Checklist

#### 5.1 Time
```
"The time complexity is O(n) because we go through the array once.
 Each lookup in the hash map is amortized O(1)."
```

#### 5.2 Space
```
"The space complexity is O(n) for the hash map.
 If we ignore the output, the auxiliary space is also O(n)."
```

#### 5.3 Trade-off (extra credit)
```
"We could reduce space to O(1) by sorting first, but time would become O(n log n).
 Given the input size, the current trade-off is better."
```

---

## 🟪 CLOSING — Follow-up Hooks

End with one of:
```
"If the input were too large to fit in memory, I would use ___ (streaming / external sort)."
"If we had to handle multiple queries, I would precompute ___."
"If this were a real-time stream, I would use ___."
"Would you like me to extend this for ___?"
```

---

## 🛡️ Stuck? Use these scripts (no shame)

```
"Let me think out loud for a moment."
"Can I take a minute to think about this?"
"Let me try a small example to see the pattern."
"I am not sure about this part — could you give me a hint?"
"Let me re-read the problem to make sure I did not miss anything."
```

When interviewer pushes back:
```
"That is a good point. Let me reconsider."
"You are right — my approach has an issue with that case."
"I see what you mean. The better approach is ___."
```

---

## 🏆 Scoring Rubric (memorize what they grade)

| Phase | What they're scoring |
|---|---|
| **Clarify** | Did you ask about size, edge cases, definitions? OR did you assume? |
| **Plan** | Did you state brute force first? Did you justify your data structure? |
| **Code** | Clean naming, validation, helpers, no duplicate logic, type hints |
| **Test** | Did you proactively name edge cases, or wait to be prompted? |
| **Complexity** | Did you state both, with reasoning? Did you discuss trade-offs? |
| **Communication** | Were you silent? Did you take hints gracefully? |

> 🔑 **Golden rule**: An interviewer's hint is a GIFT. They want you to pass. Take the hint, say "thank you, that's a good point," and pivot.
