#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
def reducer():
    current_word = None
    word = None
    count = 0
    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t')
        count = int(count)
        if word == current_word:
            current_count += count
        else:
            # False if current_word==None
            if current_word:
               print("%s\t%s" % (current_word, current_count))
            current_count = count
            current_word = word
    if current_word == word:
        print("%s\t%s" % (current_word, current_count))

if __name__ == "__main__":
    reducer()
