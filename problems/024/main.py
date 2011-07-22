# coding: utf8

import unittest

class PermutationsOf012TestCase(unittest.TestCase):

    def setUp(self):
        self.sequence = LexicograficPermutation(range(3))

    def test_1st_lexicografic_permutation_element(self):
        assert self.sequence[0] == '012'

    def test_2nd_lexicografic_permutation_element(self):
        assert self.sequence[1] == '021'

    def test_3rd_lexicografic_permutation_element(self):
        assert self.sequence[2] == '102'

    def test_4th_lexicografic_permutation_element(self):
        assert self.sequence[3] == '120'

    def test_5th_lexicografic_permutation_element(self):
        assert self.sequence[4] == '201'

    def test_6th_lexicografic_permutation_element(self):
        assert self.sequence[5] == '210'

    def test_7th_lexicografic_permutation_element(self):
        self.assertRaises(KeyError, self.sequence.__getitem__, 6)


class PermutationsOf0123456789TestCase(unittest.TestCase):

    def setUp(self):
        self.sequence = LexicograficPermutation(range(10))

    def test_1st_lexicografic_permutation_element(self):
        assert self.sequence[0] == '0123456789'

    def test_2nd_lexicografic_permutation_element(self):
        assert self.sequence[1] == '0123456798'

    def test_3rd_lexicografic_permutation_element(self):
        assert self.sequence[2] == '0123456879'

    def test_4th_lexicografic_permutation_element(self):
        assert self.sequence[3] == '0123456897'

    def test_5th_lexicografic_permutation_element(self):
        assert self.sequence[4] == '0123456978'

    def test_6th_lexicografic_permutation_element(self):
        assert self.sequence[5] == '0123456987'

    def test_7th_lexicografic_permutation_element(self):
        assert self.sequence[6] == '0123457689'

    def test_1000000th_lexicografic_permutation_element(self):
        assert self.sequence[1000000-1] == '2783915460'


class LexicograficPermutation(dict):

    def __init__(self, symbols):
        self.symbols = sorted(symbols)
        self.len = len(symbols)

    def __getitem__(self, item):
        if not item in self:
            self[item] = self._calculate_item(item)
        return super(LexicograficPermutation, self).__getitem__(item)
    
    def _calculate_item(self, item):
        n_permutations = factorial(self.len)
        if not item < n_permutations:
            raise KeyError
        ret = ''
        current_symbols = list(self.symbols)
        current_value = 0
        for i in range(self.len):
            n_permutations /= self.len - i
            i_symbol = (item-current_value)/n_permutations
            current_symbol = current_symbols[i_symbol]
            ret += str(current_symbol)
            current_symbols.remove(current_symbol)
            current_value += i_symbol * n_permutations
        return ret

def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))