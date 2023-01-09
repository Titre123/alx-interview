#!/usr/bin/python3
"""
This is unlock boxes
"""
def canUnlockAll(boxes):
    # Set to keep track of which boxes have been opened
    opened = set()
    # Start with the first box
    opened.add(0)
    # Create a queue to perform a breadth-first search
    queue = [0]

    # Perform a breadth-first search to find all the keys
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key not in opened:
                opened.add(key)
                queue.append(key)

    # Return whether all the boxes have been opened
    return len(opened) == len(boxes)
