# 🎤 Interview English Phrasebook

Memorize these. Use the SAME phrases on every problem. Do not invent new wording under stress.

---

## Phase 1 — Clarify (1–2 min)

```
"Let me make sure I understand the problem correctly."
"What is the size of the input? How large can n be?"
"Can the input be empty? Can it contain duplicates? Can values be negative?"
"Is there exactly one answer, or could there be multiple?"
"Let me walk through one example to confirm."
```

---

## Phase 2 — Plan (2–3 min)

```
"My first approach would be brute force."
"For every element, I would check every other element."
"That gives us O(n squared) time and O(1) space. It works, but I think we can do better."
"I notice that we are doing repeated work."
"If I use a hash map to remember what I have seen, I can look it up in O(1)."
"This gives us O(n) time and O(n) space. We trade space for time."
"Does this approach sound good before I start coding?"
```

---

## Phase 3 — Code (15–20 min, speak while typing)

```
"I will iterate through the array."
"For each number, I check if its complement is in the map."
"If yes, I return the two indices."
"If no, I store the current number with its index."
"I will use a helper function here to keep the code clean."
"Let me also validate the input first."
```

---

## Phase 4 — Test (3–5 min)

```
"Let me trace through with a small example."
"Now let me check edge cases:"
"  - What if the array is empty?"
"  - What if there are duplicates?"
"  - What if no valid pair exists?"
"I think the code is correct."
```

---

## Phase 5 — Complexity (1 min)

```
"The time complexity is O(n) because we go through the array once."
"The space complexity is O(n) because the hash map can hold up to n items."
"We could also discuss the trade-off — we use more memory to save time."
```

---

## When stuck (very important)

```
"Let me think out loud for a moment."
"Can I take a minute to think about this?"
"Let me try a small example to find the pattern."
"I am not sure about this part. Could you give me a hint?"
"Let me re-read the problem to make sure I did not miss anything."
```

---

## When pushing back / clarifying

```
"That is a good point. Let me reconsider."
"You are right, my approach has a problem with that case."
"Let me fix it. I think I should..."
"I see what you mean. The better approach is..."
```

---

## Closing the problem

```
"Let me summarize: the algorithm is O(n) time and O(n) space."
"If we needed to handle a larger input, we could..."
"Are there any follow-up questions you would like to explore?"
```
