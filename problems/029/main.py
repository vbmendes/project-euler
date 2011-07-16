# coding: utf8

import unittest

class ProjectEuler29TestCase(unittest.TestCase):

    def test_n_combinations_between_2_and_5(self):
        self.assertEquals(15, n_combinations(range(2, 5+1), range(2, 5+1)))

    def test_n_combinations_between_2_and_100(self):
        self.assertEquals(9183, n_combinations(range(2, 100+1), range(2, 100+1)))


def n_combinations(base_range, pow_range):
    combinations = set()
    for base in base_range:
        for pow in pow_range:
            combinations.add(base**pow)
    return len(combinations)
