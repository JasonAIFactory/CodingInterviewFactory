# Step 03 — Input Size (CRITICAL)

## 🎯 Purpose
The maximum size of `n` decides what complexity is acceptable.
Skipping this question = guessing at the wrong algorithm.

## 🧠 What interviewer is testing
Whether you can match algorithm to scale. Senior engineers ask this FIRST.

## 🇬🇧 English phrases

```
"What is the maximum size of n?"
"How large can the input be?"
"What is the upper bound on the array length?"
"Is n in the hundreds, thousands, or millions?"
```

## 🔊 How to SAY numbers and complexities out loud

### 큰 숫자 발음 (★ 외워두면 입에서 바로 나옴)

| 표기 | 영어 발음 (자연스러운 버전) | 한국어 가이드 |
|---|---|---|
| `10` | "ten" | 텐 |
| `100` | "one hundred" / "a hundred" | 헌드러드 |
| `1,000` | "one thousand" / "a thousand" | 따우전드 |
| `10,000` | "ten thousand" | 텐 따우전드 |
| `100,000` | "a hundred thousand" | 헌드러드 따우전드 |
| `10⁶` | "**one million**" or "**ten to the six**" | 밀리언 (가장 자연스러움) |
| `10⁷` | "ten million" | 텐 밀리언 |
| `10⁸` | "a hundred million" | 헌드러드 밀리언 |
| `10⁹` | "**one billion**" or "**ten to the nine**" | 빌리언 |
| `10¹²` | "one trillion" | 트릴리언 |

> 💡 **Tip**: 숫자를 말할 때 `10^6` 보다 `one million` 이 훨씬 자연스럽고 면접관이 즉시 이해함.

### 복잡도 (Big-O) 발음

| 표기 | 영어 발음 |
|---|---|
| `O(1)` | "**oh of one**" or "**constant time**" |
| `O(log n)` | "**oh of log n**" |
| `O(n)` | "**oh of n**" or "**linear time**" |
| `O(n log n)` | "**oh of n log n**" |
| `O(n²)` | "**oh of n squared**" |
| `O(n³)` | "**oh of n cubed**" |
| `O(2ⁿ)` | "**oh of two to the n**" |
| `O(n!)` | "**oh of n factorial**" |
| `O(√n)` | "**oh of square root n**" |
| `O(n + m)` | "**oh of n plus m**" |

### 자주 쓰는 실전 표현

```
"n is up to one million."
"n can be as large as ten to the nine."
"So we need an O of n solution, not O of n squared."
"With n squared, it would be 10 to the 12 operations — too slow."
"This is constant time per operation, so O of one."
"Sorting takes n log n, which is fine for n up to ten million."
```

## 🎤 Example interview dialog

```
Interviewer: "Find pairs that sum to k in this array."

You: "What is the maximum size of n?"

Interviewer: "n can be up to one million."

You: "OK, so n is one million.
      That means O of n squared — which would be ten to the twelve operations —
      is too slow.
      I need O of n or O of n log n.
      I'll use a hash map for O of n. Sound good?"
```

이 dialog 그대로 외우면 input size 단계는 완벽.

## 📚 Required knowledge — MEMORIZE THIS TABLE

| n size | Acceptable complexity | Algorithms that fit |
|---|---|---|
| **n ≤ 12** | O(n!) | Permutations, brute backtracking |
| **n ≤ 25** | O(2ⁿ) | Bitmask DP, subset enumeration |
| **n ≤ 100** | O(n³) | Triple nested loop, Floyd-Warshall |
| **n ≤ 5,000** | O(n²) | DP, nested loop, simple sort |
| **n ≤ 10⁶** | O(n log n) or O(n) | Sort, sliding window, hash map |
| **n ≤ 10⁹** | O(log n) or O(1) | Binary search, math formula |
| **n = ∞ (stream)** | O(1) per element | One-pass, online algorithm |

> 💡 If interviewer says "n is up to 10⁶", and you propose O(n²) — they'll push back.

## 📝 Reverse mapping (when interviewer hints complexity)

| If they say... | Means... |
|---|---|
| "We have a billion records" | O(n) or O(log n) only |
| "Limit is 100" | Brute force is fine |
| "Real-time" | O(1) or O(log n) per query |
| "Memory is tight" | O(1) extra space |

## ⚠️ Common mistakes

- Not asking → writing O(n²) when n = 10⁶
- Asking but not USING the answer to guide approach
- Saying "I'll use sorting" without checking if O(n log n) fits

## 🔁 Drill (cover the right column, answer out loud — IN ENGLISH)

| n max | Acceptable complexity? (say it!) |
|---|---|
| 20 | "Oh of two to the n is fine" |
| 1,000 | "Oh of n squared works" |
| 100,000 | "Oh of n log n" |
| 10⁷ (ten million) | "Oh of n" |
| 10¹⁰ (ten billion) | "Oh of log n only" |

### 입풀기 연습 (5번씩 소리내어 읽기)

```text
"What is the maximum size of n?"
"n is up to one million."
"n is up to ten to the nine."
"So we need O of n log n or better."
"O of n squared is too slow because it would be ten to the twelve."
"A hash map gives us O of one lookup, so total is O of n."
```

Bonus dialog:
> *"Given n equals 10⁵, and we need pairs that sum to k — what complexity must I aim for?"*
>
> Answer out loud: *"With n at one hundred thousand, O of n squared is ten to the ten — too slow.
> I need O of n with a hash map, or O of n log n with sort plus two pointers."*
