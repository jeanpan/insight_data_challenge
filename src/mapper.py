#!/usr/bin/env python

import sys

for line in sys.stdin:
    # remove extra whitespace
    line = line.strip()
    # split line into words
    words = line.split()
    # count every word to 1
    for word in words:
        print '%s\t%s' % (word, 1)