#!/usr/bin/python3
"""
Solution to the nqueens problem using backtracking
"""
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        # if required number of argument is used
        print("Usage: nqueens N")
        sys.exit(1)
    else:
        try:
            n = int(sys.argv[1])
            if n < 4:
                print("N must be at least 4")
        except:
            print("N must be a number")
            sys.exit(1)
