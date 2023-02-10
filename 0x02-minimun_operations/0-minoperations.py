#!/usr/bin/python3
"""
This modules provides a
function to solve the minimum operation problem,
"""
import sys


def minOperations(n):
    """
    function calculates the fewest number of operations needed to result
    in exactly n "H" characters in the file

    Args:
        n (int): number of "H" characters to find

    Return:
        An integer that shows the number of operations to achieve n "H"
    """
    if not n or (type(n) != int):
        return 0
    operations = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            operations += min_ops
            n /= min_ops
        min_ops += 1
    return operations
