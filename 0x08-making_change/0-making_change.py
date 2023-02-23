#!/usr/bin/python3
'''
    Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.
    Prototype: def makeChange(coins, total)
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each denomination
    of coin in the list Your solution's runtime will be evaluated in this task
'''


def makeChange(coins, total):
    '''
        Args:
            - coins: list
            - total: int
        Return:
            - int
    '''
    if total <= 0:
        return 0
    sorted_coins = list(reversed(sorted(coins)))
    count = 0
    i = 0
    while total > 0:
        coin = sorted_coins[i]
        if i == len(coins) - 1 and total - coin < coin:
            return -1
        if coin <= total:
            total = total - coin
            count = count + 1
        if total < coin and i != len(coins) - 1:
            i = i + 1
    return count

print(makeChange([1256, 54, 48, 16, 102], 1453))