#!/usr/bin/env python

import sys

def unique_word_count(str):
    words = set()
    for w in str.split():
        words.add(w)

    return len(words)

def get_stream_median(list, num):
    # add num 
    list.append(num)

    # sort the list (insertion sort)
    current = num
    index = len(list) - 1

    while index > 0 and list[index - 1] > current:
        list[index] = list[index - 1]
        index = index - 1

    list[index] = current

    # get the median
    lens = len(list)

    if lens % 2 != 0:
        mid = (lens / 2)
        return float(list[mid])
    else:
        left = (lens / 2) - 1
        right = (lens / 2)
        return float(list[left] + list[right]) / float(2)    


alist = []
for line in sys.stdin:
    # remove extra whitespace
    line = line.strip()
    # get unique word count 
    count = unique_word_count(line)
    # get median
    print get_stream_median(alist, count)


