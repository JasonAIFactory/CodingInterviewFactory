# String (`str`)

**Immutable** in Python.

## 🎯 Essence (memorize this one line)

> *"Like array but immutable. Don't concat in a loop — use list and join."*

## ✅ Pros / ❌ Cons

- ✅ Hashable — safe as dict key
- ❌ Immutable — can't modify in place
- ❌ `s += ch` in loop = O(n²)

## 🔵 Use when

- Text processing
- Dict key
- Comparison / equality

## 💡 Trade-off — building strings

- ❌ Concat in loop: O(n²)
- ✅ List + `"".join()`: O(n)

## 🇬🇧 What to say

- *"Strings in Python are immutable."*
- *"I'll build with a list and join at the end — concat in a loop is O of n squared."*
- *"For character arithmetic I use ord and chr."*
