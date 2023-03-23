#!/usr/bin/python3
"""
Module defines a function makeChange()
"""


def makeChange(coins, total) -> int:
    """
    Determines the fewest number of coins needed to
    meet a given amount total.

    Args:
        coins (list): an array of coins of different denomination
        total (int): the number of coins needed to meet
    Return:
        int: 0 if total is less than 0, -1 if total cannot be met
        number of coins needed to meet total
    """
    if total <= 0:
        return 0
    if len(coins) == 0 or coins is None:
        return -1

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    return count if total == 0 else -1
