#!/usr/bin/python3
'''
    Create a function def island_perimeter(grid): that returns
    the perimeter of the island described in grid
'''


def island_perimeter(grid):
    '''
        grid: list
    '''
    if type(grid) != list:
        return 0
    i = 0
    perimeter = 0
    while i < len(grid):
        arr = grid[i]
        j = 0
        while j < len(arr):
            cell = arr[j]
            if (cell == 1):
                cell_perimeter = 4
                left_side = arr[j - 1]
                right_side = arr[j + 1]
                top = grid[i - 1][j]
                bottom = grid[i + 1][j]
                other_pos = [top, bottom, left_side, right_side]
                if(other_pos.count(1) == 4):
                    cell_perimeter -= other_pos.count(1)
                elif (other_pos.count(1) == 3):
                    cell_perimeter -= other_pos.count(1)
                elif (other_pos.count(1) == 2):
                    cell_perimeter -= other_pos.count(1)
                elif (other_pos.count(1) == 1):
                    cell_perimeter -= other_pos.count(1)
                perimeter += cell_perimeter
            j = j + 1
        i = i + 1
    return perimeter
