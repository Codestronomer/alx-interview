#!/usr/bin/python3


"""
Module: 0-Lockboxes.py
Problem: You have n number of locked boxes in front of you. 
Each box is numbered sequentially from 0 to n - 1 and 
each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.

- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""

def canUnlockAll(boxes):
    """
    Traverses list and returns True if all boxes in the list
    are opened otherwise, returns False.
    """
    if not boxes or type(boxes) is not list:
        return False
    #if (len(boxes)) == 0:
    #   return False
    unlocked = boxes[0]
    for i in boxes[0]:
        for j in boxes[i]:
            if (j != i) or (j == i + 1):
                unlocked.append(i + 1)
    for i in range(1, len(boxes)):
        if i not in unlocked:
            return False
    return True
