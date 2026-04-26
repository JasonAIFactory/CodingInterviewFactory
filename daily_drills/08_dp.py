"""
08_dp.py — Daily drill (type from zero, no peeking)

Target: under 10 minutes.
Patterns: top-down memoization, bottom-up tabulation, 1D DP.
"""

from functools import lru_cache


# === Drill 1: Climbing Stairs ===
# n stairs, can climb 1 or 2 at a time. Return number of distinct ways.
def climb_stairs(n: int) -> int:
    pass


# === Drill 2: House Robber ===
# Cannot rob two adjacent houses. Return max money.
def rob(nums: list[int]) -> int:
    pass


# === Drill 3: Coin Change ===
# Coins (unlimited each), amount. Return fewest coins to make amount.
# Return -1 if impossible.
def coin_change(coins: list[int], amount: int) -> int:
    pass


# === Tests ===
if __name__ == "__main__":
    # Climb Stairs
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    assert climb_stairs(45) == 1836311903   # large to test efficiency

    # House Robber
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([2, 1, 1, 2]) == 4
    assert rob([5]) == 5
    assert rob([]) == 0

    # Coin Change
    assert coin_change([1, 2, 5], 11) == 3   # 5+5+1
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1, 2, 5], 100) == 20

    print("✅ All DP drills passed.")
