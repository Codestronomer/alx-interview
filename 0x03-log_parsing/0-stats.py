#!/usr/bin/python3
"""
This module parses logs
"""

import sys
import re

line_count = 0
total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
regex = re.compile(r"^([0-9]*\.){3}\d* - \[(\d+-){2}\d+ "
                   r"(\d+:){2}\d+.\d+] \"\w+ /\w+/\d+ \w+/\d.\d\" \d+ \d+"
                   )
for line in sys.stdin:
    if 'EXIT' == line.rstrip() or line_count == 10:
        print("File size: {}".format(total_size))
        for code, count in sorted(status_codes.items()):
            if count != 0:
                print("{}: {}".format(code, count))
        line_count = 0
        total_size = 0
        status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                        '403': 0, '404': 0, '405': 0, '500': 0}
    if not re.match(regex, line):
        continue
    values = line.split()
    total_size += int(values[-1])
    status_codes[values[-2]] += 1
    line_count += 1
