#!/usr/bin/python3
'''
write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
'''


def minOperations(n):
  '''
  Args: n
  '''
    if n == 0:
        return 0
    operations = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            operations += i
            n /= i
        i += 1
    if n > 1:
        operations += n
    return operations
