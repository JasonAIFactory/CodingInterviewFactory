# Step 09 — Walk Through the Given Example

## 🎯 Purpose
Trace the example the interviewer gave — out loud — to confirm you understood.

## 🧠 What interviewer is testing
Whether you actually understood, or just nodded politely.

## 🇬🇧 English phrases

```
"Let me walk through the given example to confirm my understanding."
"With nums = [2, 7, 11, 15] and target = 9, I expect to return [0, 1]
 because nums[0] + nums[1] = 9."
"Going step by step: at index 0 we see 2, then at index 1 we see 7,
 their sum is 9, so we return their indices."
```

## 📚 Required knowledge

**The pattern: state → step → result**

> 1. State the example: *"Input is X, expected output is Y."*
> 2. Walk through 1–3 steps: *"At step 1, this happens. At step 2..."*
> 3. Confirm the result: *"So the final answer is Y."*
> 4. Ask: *"Is that the expected behavior?"*

**Always trace WITH CONCRETE VALUES, not abstract.**

❌ Bad: "We loop and find the pair."
✅ Good: "i=0 num=2, complement=7, not in map, store. i=1 num=7, complement=2, found in map at index 0, return [0, 1]."

## ⚠️ Common mistakes

- Just saying "OK that example makes sense" → no proof of understanding
- Tracing too fast, skipping steps
- Not asking for confirmation at the end

## 🔁 Drill

Trace each example out loud:

1. **`reverse_string("hello")` → `"olleh"`**
   Walk through: take each char from the end, build new string.

2. **`is_palindrome("racecar")` → `True`**
   Walk through: r==r, a==a, c==c, middle e — palindrome.

3. **`max_depth(tree)` where root=1, left=2, right=3, with 2.left=4** → 3
   Walk: depth(4)=1, depth(2)=2, depth(3)=1, root max=2, +1 = 3.
