#!/usr/bin/python3
'''0-state is script to parse log'''
import sys


# keep track of the number
number = 0
status_code = [200, 301, 400, 401, 403, 404, 405, 500]
size = 0
status_count = {}
lines = sys.stdin.readlines()
if len(lines) == 0:
    print('File size: 0')
for line in lines:
    number += 1
    print(number)
    # parse the line of the standard input
    listed = line.split()
    if len(listed) < 6:
        continue
    parsed_list = listed[len(listed) - 2:len(listed)]

    if parsed_list != []:
        try:
            status = int(parsed_list[0])
        except ValueError:
            status = parsed_list[0]

    if status in status_code:
        size += int(parsed_list[1])
        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1
    else:
        size += int(parsed_list[1])

    try:
        if number % 10 == 0 or number == len(lines):
            print('File size: {}'.format(size))
            for status in status_code:
                if status in status_count:
                    print('{}: {}'.format(status, status_count[status]))

    except (KeyboardInterrupt, EOFError):
        print('File size: {}'.format(size))
        for status in status_code:
            if status in status_count:
                print('{}: {}'.format(status, status_count[status]))
