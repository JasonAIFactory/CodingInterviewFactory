# Trie (Prefix Tree)

**O(L) prefix search** — independent of total keys.

## 🎯 Essence (memorize this one line)

> *"Tree by character. O of L per operation, regardless of how many words stored."*

## ✅ Pros / ❌ Cons

- ✅ O(L) prefix lookup regardless of N keys
- ✅ Perfect for autocomplete / dictionary
- ❌ High memory (one node per char)
- ❌ No built-in in Python

## 🔵 Use when

- Autocomplete / suggestion
- "Find all words with prefix"
- Word Search II (Trie + backtracking)
- Spell-check

## 💡 Trade-off (vs Hash Set)

- Trie: O(L) prefix search
- Hash set: O(N × L) to scan for prefix
- Pick trie for prefix-heavy workloads

## 🇬🇧 What to say

- *"Trie gives O of L for prefix search regardless of total words."*
- *"Each node stores a children dict and an is_word flag."*
- *"I use `__slots__` to save memory — tries can have many nodes."*
