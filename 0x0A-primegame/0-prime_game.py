#!/usr/bin/python3
'''
return who won the games and return most win
    return array of winners and count of user > 1/2 of games
'''
# To know who won the game
'''
    get the game value
    loop the game value and get all possible value from 0-value
    use a method to get a prime number from an array and del the
    number from the array and multiple of the number
'''


def isPrime(value):
    '''
        @value: int
        Check if @value is a prime number
    '''
    isPrime = True
    if value == 1:
        return False
    for i in range(2, value):
        if value % i == 0 and i != value:
            return False
    return True


def Prime(array):
    '''
        pick a prime number for the user
    '''
    for num in array:
        if (isPrime(num)):
            return num
    return None


def playTurn(array):
    '''
        @array: int
        remove element from array after each player plays
    '''
    pick_prime = Prime(array)
    for num in array:
        if num % pick_prime == 0:
            array.remove(num)
    return array


def formArr(num):
    '''
        @num: int
        create an arrage of consecutive number till tne @num
    '''
    arr = []
    for i in range(1, num+1):
        arr.append(i)
    return arr


def playGame(num):
    '''
        num: int
        Return: Winner of a round
    '''
    game_arr = formArr(num)
    player_playing = 'Maria'
    while True:
        # player_1 trun
        if player_playing == 'Maria':
            game_arr = playTurn(game_arr)
            if game_arr[0] and len(game_arr) == 1:
                break
            player_playing = 'Ben'
        #  player_2 turn
        if player_playing == 'Ben':
            game_arr = playTurn(game_arr)
            if game_arr[0] and len(game_arr) == 1:
                break
            player_playing = 'Maria'
    return player_playing


def isWinner(x, nums):
    '''
        x: int,
        nums: int
    '''
    winners = []
    for num in nums:
        if num != 1:
            winners.append(playGame(num))
        else:
            winners.append('Ben')
    if winners.count('Ben') > x / 2:
        return 'Ben'
    elif winners.count('Maria') > x / 2:
        return 'Maria'
    else:
        return 'Draw'
