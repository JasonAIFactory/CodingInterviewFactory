"""
01_class_basics_practice.py  —  TYPE FROM SCRATCH

Build a BankAccount class that passes the tests at the bottom.
Do not look at the reference.
"""


class BankAccount:
    # TODO: class attribute bank_name = "AmazonBank"

    def __init__(self, owner, balance=0.0):
        # TODO: self.owner = owner
        # TODO: self._balance = balance
        pass

    # TODO: deposit(self, amount):
    #         validate amount, then add to _balance

    # TODO: withdraw(self, amount):
    #         validate amount, raise if amount > _balance, else subtract

    # TODO: @property balance(self) returns self._balance

    # TODO: _validate_amount(self, amount):
    #         raise ValueError("Amount must be positive") if amount <= 0

    # TODO: @classmethod from_dict(cls, data) -> BankAccount

    # TODO: @staticmethod is_valid_owner_name(name) -> bool


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    acc = BankAccount("Daeseon", 100)
    acc.deposit(50)
    acc.withdraw(30)
    assert acc.balance == 120
    assert acc.owner == "Daeseon"

    acc2 = BankAccount.from_dict({"owner": "Alice", "balance": 200})
    assert acc2.owner == "Alice"
    assert acc2.balance == 200

    assert BankAccount.is_valid_owner_name("") is False
    assert BankAccount.is_valid_owner_name("Bob") is True
    assert BankAccount.bank_name == "AmazonBank"

    # Validation tests
    try:
        acc.deposit(-5)
        assert False, "should have raised"
    except ValueError:
        pass

    try:
        acc.withdraw(99999)
        assert False, "should have raised"
    except ValueError:
        pass

    print("✅ All tests passed.")
