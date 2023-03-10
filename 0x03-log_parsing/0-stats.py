#!/usr/bin/python3
"""
This module parses logs
"""

import sys
import re


total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}


def printstats():
    """
    prints the required statistics gotten from the logs
    Args:
        None
    Return:
        None
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print("{}: {}".format(code, count))


try:
    for i, line in enumerate(sys.stdin, start=1):
        try:
            values = line.rstrip().split()
            total_size += int(values[-1])
            status_codes[values[-2]] += 1
        except Exception:
            pass
        if i % 10 == 0:
            printstats()
    printstats()
except KeyboardInterrupt:
    printstats()
    raise
