# 0x0A-primegame

## Objective
To build a program that determine the winner of a game

## Solution

```
def isWinner(x, nums):
    '''
        x: int,
        nums: int
    '''
    winners = []
    for num in array:
        if num != 1:
            winners.append(playGame(num))
        else:
            winners.append('Ben')
    if winners.count('Ben') > n / 2:
        return 'Ben'
    elif winners.count('Maria') > n / 2:
        return 'Maria'
    else:
        return 'Draw'
```

## Credit
Taiwo Ola-Balogun