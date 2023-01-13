#!/usr/bin/python3
'''
write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
'''


def minOperations(n):
    '''
    Args: n
    '''
    operation = 0
    if n <= 1 or not isinstance(n, int):
        return 0
    while n > 1:
        if(n % 2 == 0):
            operation += 2
            n = n / 2
        elif (n % 3 == 0):
            operation += 3
            n = n / 3
        elif (n % 5 == 0):
            operation += 5
            n = n / 5
        elif (n % 7 == 0):
            operation += 7
            n = n / 7
        else:
            operation += n
            n = n / n
    return operation
