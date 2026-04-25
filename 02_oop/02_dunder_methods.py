"""
02_dunder_methods.py  —  REFERENCE FILE

Goal: Make your custom objects behave like built-ins.
Dunder = "double underscore" methods like __init__, __eq__, __lt__.

Why this matters: When the interviewer asks you to put your objects into
a set, dict, sort them, or push to a heap — they ONLY work if you implement
the right dunder methods.
"""


class Card:
    """
    A playing card. Supports printing, equality, hashing, and sorting.
    """

    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def __init__(self, rank: int, suit: str):
        # SAY: "Rank is 2 to 14 (Ace high). Suit is one of four strings."
        self.rank = rank
        self.suit = suit

    # ---- Printing ----

    def __repr__(self) -> str:
        # SAY: "__repr__ is for developers. It should be unambiguous.
        #       It also gets used when I print a list of cards."
        return f"Card({self.rank}, {self.suit!r})"

    def __str__(self) -> str:
        # SAY: "__str__ is for users. Falls back to __repr__ if not defined."
        return f"{self.rank} of {self.suit}"

    # ---- Equality + hashing (so cards can go in sets and dicts) ----

    def __eq__(self, other) -> bool:
        # SAY: "Two cards are equal if rank and suit both match."
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self) -> int:
        # SAY: "Hash MUST be consistent with __eq__.
        #       Equal objects must have equal hashes."
        return hash((self.rank, self.suit))

    # ---- Ordering (so cards can be sorted or pushed to a heap) ----

    def __lt__(self, other: "Card") -> bool:
        # SAY: "Less-than enables sorting and heapq.
        #       I compare rank first, then suit as a tiebreaker."
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.SUITS.index(self.suit) < self.SUITS.index(other.suit)


# ============================================================
# Why this matters in interviews — see the difference
# ============================================================

if __name__ == "__main__":
    a = Card(10, "Hearts")
    b = Card(10, "Hearts")
    c = Card(7, "Spades")

    # __repr__ in action
    print([a, b, c])

    # __eq__ + __hash__ → set works
    unique = {a, b, c}
    print(len(unique))                  # 2 (a and b are equal)

    # __lt__ → sorted works
    print(sorted([a, c]))               # 7 of Spades first

    # Equal hashes for equal objects
    assert hash(a) == hash(b)
