#!/usr/bin/python3
"""
Module contains a list of lists of integers representing
the pascal's triangle of integer n
"""

def pascal_triangle(n):
    """function that returns a pascal triangle"""
    if n <= 0:
        return []
    arr = []
    for i in range(0, n + 1):
        c = 1
        arr2 = []
        for i in range(1, i+1):
            arr2.append(i)
        arr.append(arr2)
    return arr
