#!/usr/bin/python3
'''0-state is script to parse log'''


def validUTF8(data):
    """
        Args:
            - data
    """
    return True if sorted(data)[len(data) - 1] < 128 else False
