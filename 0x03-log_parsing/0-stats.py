
'''0-state is script to parse log'''
import sys


# keep track of the number
number = 0
status_code = [200, 301, 400, 401, 403, 404, 405, 500]
size = 0
status_count = {}
for line in sys.stdin:
    number += 1
    # parse the line of the standard input
    parsed_list = line.split()[7:9]
    status = int(parsed_list[0])

    if status in status_code:
        size += int(parsed_list[1])
        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1

    try:
        if number % 10 == 0:
            print('File size: {}'.format(size))
            for status in status_code:
                if status in status_count:
                    print('{}: {}'.format(status, status_count[status]))

    except (KeyboardInterrupt, EOFError):
        print('File size: {}'.format(size))
        for status in status_code:
            if status in status_count:
                print('{}: {}'.format(status, status_count[status]))
