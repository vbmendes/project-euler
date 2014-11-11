#!/usr/bin/env python

def even_fibbonacci(limit):
    current = 1
    previous = 1
    while(current <= limit):
        if not current % 2:
            yield current
        current, previous = current + previous, current

print sum(n for n in even_fibbonacci(4000000))
