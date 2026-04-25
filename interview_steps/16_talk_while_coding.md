# Step 16 — Talk While Coding ⭐

## 🎯 Purpose
Narrate your code as you write it. Silent typing = automatic deduction.

## 🧠 What interviewer is testing
Communication. Ability to think out loud. Whether they can follow your reasoning.

## 🇬🇧 English phrases (block-by-block narration)

```
"I will create an empty hash map called seen."
"I will iterate with enumerate so I have both index and value."
"For each number, I compute the complement which is target minus num."
"If the complement is already in the map, I return the stored index and the current index."
"Otherwise, I add the current number to the map with its index."
"At the end, if no pair was found, I return an empty list."
```

## 📚 Required knowledge — what level to narrate at

**❌ Too detailed (annoying):**
> *"I'm typing 'i', then space, then '=', then space, then 'zero'..."*

**❌ Too vague (useless):**
> *"OK I'll write the loop now... done."*

**✅ Just right (block-level):**
> *"I'm initializing the result list and the seen map. Now I start the main loop."*

## 🔑 The pattern: narrate INTENT, not syntax

**Per code block, say one sentence:**
1. What you're about to write
2. Why

```python
# SAY: "I'll create a hash map to track seen values, mapping number to its index."
seen: dict[int, int] = {}

# SAY: "I loop with enumerate to get both index and value."
for i, num in enumerate(nums):
    # SAY: "Compute the complement — what we'd need to pair with num."
    complement = target - num

    # SAY: "If we've already seen the complement, we found our pair."
    if complement in seen:
        return [seen[complement], i]

    # SAY: "Otherwise, remember this number for future lookups."
    seen[num] = i
```

## ⚠️ Common mistakes

- Going silent for 5 minutes → interviewer worries
- Narrating syntax char-by-char → slow + annoying
- Talking ABOUT the algorithm but not WHILE coding it
- Pauses with no explanation: *"hold on..."* (3 minutes silence)

## 🔁 Drill

Narrate while typing, in English (no Korean filler):

1. **`def is_palindrome(s):`** — "I define a function that takes a string and returns a boolean."
2. **`l, r = 0, len(s) - 1`** — "Two pointers — left at zero, right at the last index."
3. **`while l < r:`** — "I move pointers toward each other until they meet."
4. **`if s[l] != s[r]: return False`** — "If chars differ, it's not a palindrome — return False immediately."
5. **`l, r = l + 1, r - 1`** — "Otherwise advance both pointers."

Practice this whole flow out loud 3 times.
