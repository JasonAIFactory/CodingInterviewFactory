# Step 17 — Type Hints + Helpers + Validation (Production Style)

## 🎯 Purpose
Make your code look senior. Round 2 (Logical & Maintainable) grades this directly.

## 🧠 What interviewer is testing
Code quality, attention to interfaces, separation of concerns.

## 🇬🇧 English phrases

```
"I will add type hints to make the contract clear."
"Let me extract this into a helper to keep the main flow readable."
"I'll add input validation upfront to fail loudly on bad input."
"I want to separate the validation from the algorithm itself."
"Let me name this constant — it's clearer than a magic number."
```

## 📚 Required knowledge

### Type hints (Python 3.9+ syntax)

```python
def two_sum(nums: list[int], target: int) -> list[int]:
def group_words(words: list[str]) -> dict[int, list[str]]:
def find_node(root: TreeNode | None, target: int) -> TreeNode | None:
def count_islands(grid: list[list[str]]) -> int:
def lru_get(self, key: int) -> int:
```

Common annotations:
- `list[int]`, `dict[str, int]`, `set[str]`, `tuple[int, int]`
- `str | None` (3.10+) or `Optional[str]` (older)
- `Callable[[int], bool]` for function args
- `-> None` when returning nothing explicitly

### Input validation pattern

```python
def withdraw(self, amount: float) -> None:
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > self._balance:
        raise ValueError("Insufficient funds")
    self._balance -= amount
```

### Helper extraction pattern

❌ Long, mixed concerns:
```python
def process(self, data):
    # 30 lines of validation
    # 30 lines of parsing
    # 30 lines of computation
```

✅ Extracted helpers:
```python
def process(self, data):
    self._validate(data)
    parsed = self._parse(data)
    return self._compute(parsed)

def _validate(self, data): ...
def _parse(self, data): ...
def _compute(self, data): ...
```

### Constants vs magic numbers

❌ `for i in range(26):`
✅ `ALPHABET_SIZE = 26` then `for i in range(ALPHABET_SIZE):`

## ⚠️ Common mistakes

- Skipping type hints (looks like a script)
- One giant 50-line function (looks junior)
- No validation — silent crash on bad input
- `26`, `1000` floating in code with no name

## 🔁 Drill

Add type hints to these signatures:

1. `def fib(n):` → `def fib(n: int) -> int:`
2. `def merge(a, b):` (a, b are sorted lists) → `def merge(a: list[int], b: list[int]) -> list[int]:`
3. `def find(root, val):` (BST search) → `def find(root: TreeNode | None, val: int) -> TreeNode | None:`

Extract a helper:

> Function `summarize(data)` does: validate → parse → compute → format.  
> Refactor into 4 functions.
