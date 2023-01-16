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
        for x in range(2,50000):
            if (n % x == 0):
                operation += x
                n = n/x
                break
    # if (n > 1):
    #     operation += n
    return operation
