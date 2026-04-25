"""
01_class_basics.py  —  REFERENCE FILE

Goal: Write a clean Python class.
Why this matters: Round 2 (Logical & Maintainable) often asks you to design
a small system — Parking Lot, Logger, Rate Limiter, LRU Cache, Bank Account.
You will be judged on naming, structure, and extensibility.
"""


# ============================================================
# A simple class with __init__ and methods
# ============================================================

class BankAccount:
    """
    SAY: "I model a bank account with a balance and an owner.
          The class encapsulates state and exposes safe operations."
    """

    # Class attribute — shared across ALL instances
    bank_name = "AmazonBank"

    def __init__(self, owner: str, balance: float = 0.0):
        # SAY: "Instance attributes are set in __init__."
        self.owner = owner
        self._balance = balance          # underscore = "private by convention"

    # ---- Public methods ----

    def deposit(self, amount: float) -> None:
        # SAY: "I validate the input first to fail loudly on bad data."
        self._validate_amount(amount)
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        self._validate_amount(amount)
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    # ---- Read-only access via @property ----

    @property
    def balance(self) -> float:
        """SAY: "Property lets the caller read balance like an attribute,
                 but I control how it's exposed."""
        return self._balance

    # ---- Private helper (separation of concerns) ----

    def _validate_amount(self, amount: float) -> None:
        # SAY: "I keep validation in one place so I don't duplicate logic."
        if amount <= 0:
            raise ValueError("Amount must be positive")

    # ---- Class method = alternative constructor ----

    @classmethod
    def from_dict(cls, data: dict) -> "BankAccount":
        # SAY: "A class method receives the class itself, not an instance.
        #       I use it as an alternative constructor."
        return cls(owner=data["owner"], balance=data.get("balance", 0))

    # ---- Static method = utility, no self / cls needed ----

    @staticmethod
    def is_valid_owner_name(name: str) -> bool:
        # SAY: "A static method does not depend on instance or class state."
        return isinstance(name, str) and len(name) > 0


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    acc = BankAccount("Daeseon", 100)
    acc.deposit(50)
    acc.withdraw(30)
    print(acc.balance)                              # 120

    acc2 = BankAccount.from_dict({"owner": "Alice", "balance": 200})
    print(acc2.owner, acc2.balance)                 # Alice 200

    print(BankAccount.is_valid_owner_name(""))      # False
    print(BankAccount.bank_name)                    # AmazonBank
