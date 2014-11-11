# coding: utf8

import unittest

class SpiralMatrixTestCase(unittest.TestCase):

    def test_spiral_matrix_one(self):
        self.assertEquals([[1]], SpiralMatrix(1))

    def test_spiral_matrix_five(self):
        self.assertEquals([
            [21, 22, 23, 24, 25],
            [20,  7,  8,  9, 10],
            [19,  6,  1,  2, 11],
            [18,  5,  4,  3, 12],
            [17, 16, 15, 14, 13],
        ], SpiralMatrix(5))

    def test_sum_of_diagonals_in_spiral_matrix_five(self):
        self.assertEquals(101, SpiralMatrix(5).sum_of_diagonals())

    def _test_sum_of_diagonals_in_spiral_matrix_1001(self):
        """
        This test uses a brute force implementation but this problem can be
        solved by the formula:
            f(n) = 4*(n**2) - 6*n + 6 + f(n-2) # if n >= 3
            f(n) = 1 # if n == 1
        n must be an odd number.
        """
        self.assertEquals(669171001, SpiralMatrix(1001).sum_of_diagonals())

    def test_sum_of_diagonals_in_spiral_matrix_1001_as_forum(self):
        self.assertEquals(669171001, sum_of_spiral_diagonals(1001))

class SpiralMatrix(list):

    def __init__(self, len):
        self.len = len
        self._initialize_empty()
        self._initialize_spiral()

    def _initialize_empty(self):
        for i in range(self.len):
            self.append([])
            for j in range(self.len):
                self[i].append(0)

    def _initialize_spiral(self):
        x, y = self.len - 1, 0

        direction = 'left'
        directions = {
            'left': {
                'next': 'down',
                'change_xy': lambda x, y: (x-1, y),
                'test': lambda x, y: x == 0 or self[y][x-1] != 0,
            },
            'down': {
                'next': 'right',
                'change_xy': lambda x, y: (x, y+1),
                'test': lambda x, y: y == self.len-1 or self[y+1][x] != 0,
            },
            'right': {
                'next': 'top',
                'change_xy': lambda x, y: (x+1, y),
                'test': lambda x, y: x == self.len-1 or self[y][x+1] != 0,
            },
            'top': {
                'next': 'left',
                'change_xy': lambda x, y: (x, y-1),
                'test': lambda x, y: y == 0 or self[y-1][x] != 0,
            }
        }

        for i in range(self.len*self.len-1, -1, -1):
            self[y][x] = i + 1
            if directions[direction]['test'](x, y):
                direction = directions[direction]['next']
            x, y = directions[direction]['change_xy'](x, y)

    def sum_of_diagonals(self):
        return (sum(self[i][i] for i in range(self.len)) +
                sum(self[self.len-1-i][i] for i in range(self.len)) - 1)


def sum_of_spiral_diagonals(n):
    return sum(4*(i**2) - 6*i + 6 for i in range(3, n+1, 2)) + 1
        