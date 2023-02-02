#!/usr/bin/python3
'''0-state is script to parse log'''


def validUTF8(data):
    """
        Args:
            - data
    """
    binary = ''
    for item in data:
        bina = str(bin(item))
        new_str = bina.replace('0b', '')
        
        binary += f' {new_str}'

    return binary


# if len(new_str) < 8:
#             left = 8 - len(new_str)
#             zero_added = '0' * left
#             new = zero_added + new_str
#             binary += f' {new}'
#         elif len(new_str) > 8:
#             left = len(new_str) - 8
#             new = new_str[left:]
#             binary += f' {new}'
#         else: