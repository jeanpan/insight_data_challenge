#!/usr/bin/env python

from operator import itemgetter
import sys

word2count = {}

for line in sys.stdin:
    # remove extra whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # aggregate count
    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count
    except ValueError:
        # convert str to int error
        pass

# sort words alphabetically;
sorted_word2count = sorted(word2count.items(), key=itemgetter(0))

for word, count in sorted_word2count:
    print '%s\t%s'% (word, count)