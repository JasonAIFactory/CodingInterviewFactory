# CLAUDE.md — Project Instructions

> **Read this first whenever starting a new session.**
> All workflow + conventions to keep adding problems consistently.

---

## 🎯 Project Purpose

**Amazon SDE II coding interview prep — coding scope ONLY.**

Recruiter-confirmed structure (do NOT add behavioral / system design / OOD):

- 4 × 1-hour interviews (3 coding + 1 system design)
- Each = 30-min technical + 30-min behavioral
- **Coding = 30 minutes only** per round (this is tighter than typical practice)
- Coding env: shared doc (Google Doc / CoderPad), **NO IDE, NO AI, NO autocomplete**
- Production quality, NO pseudocode

User handles separately (DO NOT touch in this project):

- ❌ Behavioral / STAR / Leadership Principles
- ❌ System Design (HLD)
- ❌ Pure LLD / OOD (Vending Machine, Parking Lot)
- ❌ AI prep

---

## 📁 Folder Structure

```text
CodingInterviewFactory/
├── README.md
├── CLAUDE.md                        ← THIS FILE
├── interview_template.md            ← 19-step framework master
├── phrasebook.md                    ← Interview English phrases
├── leetcode_list.md                 ← User's curated problem list
│
├── 01_python_basics/                ← Python reference + practice files
├── 02_oop/                          ← Python OOP reference + practice
├── 03_patterns/                     ← Algorithm Python templates + practice
│
├── algorithms/                      ← Lean cheat cards (memorize-friendly)
├── data_structures/                 ← Lean cheat cards (memorize-friendly)
├── interview_steps/                 ← 22 step files (granular framework)
│
├── leetcode_amazon/                 ← Algorithm walkthroughs (R1, R3)
└── leetcode_amazon_design/          ← Design walkthroughs (R2)
```

---

## ✍️ How to ADD a New Problem Walkthrough (the workflow)

### Step 1: Choose the right folder

| Problem type | Folder | Examples |
|---|---|---|
| **Algorithm** (R1, R3) | `leetcode_amazon/` | Two Sum, Number of Islands, Trapping Rain Water |
| **Design** (R2) | `leetcode_amazon_design/` | LRU Cache, Min Stack, Insert Delete GetRandom |

### Step 2: Filename convention

```text
NN. snake_case_problem_name.md
```

Number sequentially — `07.`, `08.`, etc. Look at the highest existing number first.

### Step 3: Use the standard template (see below)

### Step 4: Verify the code runs

```bash
python3 -c "
[paste Final Code]
[paste a few asserts]
print('✅ All tests passed.')
"
```

### Step 5: Commit (when user asks)

---

## 📋 Walkthrough Template (REQUIRED structure)

Every walkthrough file MUST have these sections in this order:

```markdown
# {Problem Name} ({LC#}) — {Time}-min Interview Script

> {LeetCode #N (Easy/Medium/Hard) — Amazon comment.}
> Read OUT LOUD. Total: ~{X} min.

---

## 🎬 Setup
**Interviewer:** *"[short problem statement, no examples]"*
(That's all. Everything else, you ASK.)

---

## 🟦 CLARIFY (3-5 min)
### 1. Restate
### 2. Input (ask in one breath)
### 3. Output
### 4. Definition / fuzzy terms
### 5. Constraints (memory, etc.)
### 6. Example (request from interviewer)
### 7. My own example (smaller / edge)

---

## 🟦 PLAN (3-5 min)
### 8. Brute force first
### 9. Identify inefficiency ⭐
### 10. Optimization + data structure choice
### 11. Complexity upfront
### 12. Buy-in ("Sound good before I code?") ⭐

---

## 🟦 CODE (8-12 min)
### 13.0 Quick check (function vs class)
### 13.1 Approach (recap before typing)
### 13.1.5 Pseudocode-comments FIRST  ← only for design problems
### 13.2 The code (production quality, type hints, docstring)
### 13.3 What to say while typing (concise narration)
### 13.4 Naming choices

---

## 🟦 TEST (3 min)
### 15. Dry run (with example)
### 16. Edge cases (proactive list)
### 17. Off-by-one check

---

## 🟦 COMPLEXITY (1 min)
### 18. Final time + space + trade-off

---

## 🟦 CLOSE (1 min)
### 19. Follow-up extensions

---

## ⏱️ Time check (table fitting ≤ 30 min)

---

## 🔁 Drill (Rep 1 → 2 → 3 protocol)

---

## 📝 Final Code (copy-paste ready)
[Production code, with type hints, docstring]
[Optional: alternative approach if relevant]

**Complexity:** Time / Space

---

## 🧠 Pattern: ___ — what to remember
[Reusable pattern summary]

---

## 🇬🇧 What to say in interview (signature phrases)
[3-5 English lines to memorize]
```

---

## ✅ Production Quality Checklist (every Final Code)

- ✅ Type hints on EVERY function param + return: `def f(nums: list[int], target: int) -> list[int]:`
- ✅ Docstring (one-line summary)
- ✅ Use modern Python types: `list[int]`, `dict[str, int]`, `str | None` (3.10+)
- ✅ Validate inputs at boundaries (raise `ValueError` for bad input)
- ✅ Helper methods prefixed with `_` (private convention)
- ✅ Use `__slots__` on data-only classes when memory matters
- ✅ Constants in `UPPER_CASE` at module level
- ✅ NO magic numbers
- ✅ NO pseudocode in Final Code section
- ✅ Code MUST run — verify with inline `python3 -c` test before committing

---

## 🇬🇧 English Standards

- Simple sentences (CEFR B1 level)
- NO complex grammar — short and clear > eloquent
- Reuse the SAME phrases across problems
- Always include 🇬🇧 section with 3-5 memorize-able English lines
- DO NOT polish the user's English when they upload — only flag if meaning unclear or technical content wrong

See [`phrasebook.md`](phrasebook.md) and [`interview_template.md`](interview_template.md).

---

## 🎤 Mock Interview Mode

When user pastes a problem and asks for mock:

1. Act as Amazon interviewer (short statement, no examples)
2. Wait for user to ask clarifying questions
3. Answer in interviewer voice (sometimes vaguely on purpose)
4. Drop hints if stuck — but **max 1-2 hints** (excessive hand-holding = red flag for senior)
5. NEVER reveal the optimal solution before the user attempts
6. After attempt: structured feedback on Logical&Maintainable + Problem Solving rubrics
7. End with 1-2 follow-up questions

---

## 🔑 Recruiter-Confirmed Coding Facts

```text
- 30 min total per coding round
- 10-15 min: clarify + approach + complexity (BEFORE typing)
- 15-20 min: actual typing
- 5-10 min: optimize / debug

- No IDE: shared doc like Google Doc / CoderPad
- No AI / autocomplete / autocorrect
- No pseudocode — production quality
- Naming, no syntax errors, clean structure required

- Question source: LeetCode #Amazon tag, Glassdoor, Blind, Reddit
- Difficulty: Medium-Hard (occasional Easy)

- Excessive interviewer probing = RED FLAG (you didn't give detail upfront)
- Hand-holding = RED FLAG (not autonomous senior)
- Trade-offs must be DEEP (shallow = fail)
- Communicate ALL thought process out loud
```

---

## 🔄 Workflow When User Adds a New Problem

User says: *"Make walkthrough for [Problem Name]"*

1. ✅ Pick folder (`leetcode_amazon/` or `leetcode_amazon_design/`)
2. ✅ Look at highest existing number, increment for new file
3. ✅ Use the template above
4. ✅ Write Final Code with type hints + docstring
5. ✅ Run `python3 -c` inline test with assertions
6. ✅ Show user: file location + key insight + verification result
7. ✅ Wait for user instruction before committing (do NOT auto-commit)

---

## 🚫 Things NOT to Do (memory-pinned)

- ❌ Build behavioral / STAR / LP folders or guides
- ❌ Suggest System Design content
- ❌ Add OOD problems (Vending Machine, Parking Lot, Elevator)
- ❌ Suggest Pramp, Bluescape, Amazon webinars (handled separately)
- ❌ Polish user's English grammar (only flag if meaning broken)
- ❌ Push for more reps when user is moving forward
- ❌ Auto-commit — wait for user's explicit instruction

---

## 📚 Quick Reference Pointers

| For... | Look at... |
|---|---|
| 19-step framework | [`interview_template.md`](interview_template.md) |
| Per-step granular detail | [`interview_steps/`](interview_steps/) |
| Memorizable English phrases | [`phrasebook.md`](phrasebook.md) |
| Data structure cheat cards | [`data_structures/`](data_structures/) |
| Algorithm pattern cheat cards | [`algorithms/`](algorithms/) |
| Algorithm Python templates | [`03_patterns/`](03_patterns/) |
| Python tools (collections, heapq, etc.) | [`01_python_basics/`](01_python_basics/) |
| OOP basics + LRU | [`02_oop/`](02_oop/) |
| Existing algorithm walkthroughs | [`leetcode_amazon/`](leetcode_amazon/) |
| Existing design walkthroughs | [`leetcode_amazon_design/`](leetcode_amazon_design/) |

---

## 🎯 Current Plan Snapshot (15-day prep)

```text
17 problems × 3 reps = 51 walkthroughs total
- Algorithm: 12 (mostly Medium, 1-2 Hard for approach only)
- Design: 5 (LRU, Min Stack, Insert Delete GetRandom, Logger Rate Limiter, Trie)

Practice protocol per problem:
- Rep 1 (40 min): Read walkthrough OUT LOUD, type Final Code in Google Docs
- Rep 2 (25 min): Cover walkthrough, attempt cold
- Rep 3 (20 min): Solve from scratch, time it
```

---

## 🛠️ Verifying Code Before Commit

```bash
# For each new walkthrough's Final Code, run:
python3 << 'EOF'
[paste the Final Code]
[add assertions covering: example, edge cases, expected outputs]
print("✅ All tests passed.")
EOF
```

**Never commit a walkthrough whose code fails.** Fix first.

---

## 📦 Commit Convention

When user asks to commit:

```bash
git add [specific files, NOT git add .]
git commit -m "$(cat <<'EOF'
{Short summary}

{Bullet list of what was added/changed}

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
git push origin main
```
