#!/usr/bin/env python

import unittest

class ProjectEuler14TestCase(unittest.TestCase):

    def test_next_for_13_should_be_40(self):
        self.assertEquals(next_for(13), 40)

    def test_next_for_40_should_be_20(self):
        self.assertEquals(next_for(40), 20)

    def test_sequence_for_13(self):
        self.assertEquals(sequence_for(13), [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_longer_sequence_until_13(self):
        self.assertEquals(longer_sequence_until(13), sequence_for(9))

    def test_longer_sequence_until_1000000(self):
        self.assertEquals(longer_sequence_until(1000000)[0], 837799)

is_even = lambda n: not n%2

def next_for(n):
    if is_even(n):
        return n/2
    else:
        return 3*n + 1


def sequence_for(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        n = next_for(n)
    sequence.append(1)
    return sequence

def longer_sequence_until(n):
    longer = {
        'starter': 2,
        'len': 2,
        'seq': [2, 1]
    }
    for i in range(2, n+1):
        seq = sequence_for(i)
        len_seq = len(seq)
        if len_seq > longer['len']:
            longer['len'] = len_seq
            longer['starter'] = i
            longer['seq'] = seq
    return longer['seq']
