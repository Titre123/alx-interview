def canUnlockAll(boxes):
    # Set of boxes that are unlocked
    unlocked_boxes = {0}
    # Queue of boxes that we need to check
    queue = [0]

    # Perform a breadth-first search
    while queue:
        # Take the first box from the queue
        box = queue.pop(0)
        # Open all the boxes that can be opened
        for key in boxes[box]:
            if key not in unlocked_boxes:
                # Mark the box as unlocked
                unlocked_boxes.add(key)
                # Add the box to the queue
                queue.append(key)

    # Check if all boxes are unlocked
    return len(unlocked_boxes) == len(boxes)
