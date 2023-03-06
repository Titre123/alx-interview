# 0x08-making_change

## Desciption
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
Prototype: def makeChange(coins, total)
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each denomination of coin in the list
    Your solution's runtime will be evaluated in this task

## Solution sample
```
    sorted_coins = list(reversed(sorted(coins)))
    count = 0
    i = 0
    while total > 0:
        coin = sorted_coins[i]
        if coin < total:
            total = total - coin
        count = count + 1
        if i == len(coins) - 1 and total < coin:
            return -1
        if total < coin:
            i = i + 1
```

## Credit
[Taiwo Ola-Balogun]()
[Email](taiwotriumphant@gmail.com)
[LinkedIn](linkedin.com/taiwotriumphant)
[twitter](twitter.com/dumbdev)