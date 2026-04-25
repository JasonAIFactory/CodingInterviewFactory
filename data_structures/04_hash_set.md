# Hash Set (`set`)

**O(1) membership check.**

## 🎯 Essence (memorize this one line)

> *"Same as hash map but only keys. O of one membership check. Use for dedup and 'have I seen?' questions."*

## ✅ Pros / ❌ Cons

- ✅ O(1) `in` check
- ✅ Set algebra: `&` `|` `-` `^`
- ❌ No values, just keys
- ❌ No order, no indexing

## 🔵 Use when

- "Has this been seen?"
- Remove duplicates (`set(arr)`)
- Common elements between collections

## 💡 Trade-off (vs Hash Map)

- Set: just keys
- Hash map: keys → values
- Use set when you don't need values

## 🇬🇧 What to say

- *"A set works because I only need membership, not values."*
- *"Use ampersand for intersection, pipe for union."*
- *"For dedup I just call set on the array."*
