#!/usr/bin/python3
"""
Module contains a list of lists of integers representing
the pascal's triangle of integer n
"""

def pascal_triangle(n):
    """
    function returns a list of lists of integers
    representing the pascal's triangle o f n
    """

    if n <= 0:
        return []
    arr = []
    for i in range(0, n + 1):
        c = 1
        arr2 = []
        for j in range(1, i+1):
            arr2.append(c)
            c = c * (i -j) // j
        arr.append(arr2)
    return arr[1:]
