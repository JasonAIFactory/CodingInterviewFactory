"""
02_dunder_methods_practice.py  —  TYPE FROM SCRATCH

Build a Card class with __repr__, __eq__, __hash__, __lt__.
"""


class Card:
    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def __init__(self, rank, suit):
        # TODO: store rank and suit
        pass

    # TODO: __repr__ returns f"Card({self.rank}, {self.suit!r})"

    # TODO: __str__ returns f"{self.rank} of {self.suit}"

    # TODO: __eq__ returns True if both rank and suit match
    #       Return NotImplemented if `other` is not a Card

    # TODO: __hash__ returns hash((self.rank, self.suit))

    # TODO: __lt__ compares rank first, then suit index in SUITS


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    a = Card(10, "Hearts")
    b = Card(10, "Hearts")
    c = Card(7, "Spades")

    assert a == b
    assert a != c
    assert hash(a) == hash(b)

    # Sets deduplicate equal cards
    assert len({a, b, c}) == 2

    # Sorted by rank
    assert sorted([a, c]) == [c, a]

    # __repr__ format
    assert repr(a) == "Card(10, 'Hearts')"

    # __str__ format
    assert str(a) == "10 of Hearts"

    print("✅ All tests passed.")
