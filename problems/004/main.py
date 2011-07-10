#!/usr/bin/env python

def palindrome_iterator():
    for d1 in range(9,0,-1):
        for d2 in range(9,-1,-1):
            for d3 in range(9,-1,-1):
                palindrome_part = '%s%s%s' % (d1, d2, d3)
                yield int(palindrome_part + palindrome_part[::-1])

def get_palindrome():
    for palindrome in palindrome_iterator():
        for i in xrange(999, 100, -1):
            if not palindrome%i and 100 <= palindrome/i <= 999:
                return palindrome

print get_palindrome()

