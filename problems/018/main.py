# coding: utf8

import unittest

class ProjectEuler18TestCase(unittest.TestCase):

    def test_build_triangle(self):
        with open('sample_triangle.txt', 'r') as f:
            self.assertEquals(build_triangle(f.read()),
                [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])

    def test_max_sum_for_sample_triangle(self):
        with open('sample_triangle.txt', 'r') as f:
            triangle = build_triangle(f.read())
            self.assertEquals(max_sum_in_path(triangle), 23)

    def test_max_sum_for_018_triangle(self):
        with open('018_triangle.txt', 'r') as f:
            triangle = build_triangle(f.read())
            self.assertEquals(max_sum_in_path(triangle), 1074)

    def test_max_sum_for_067_triangle(self):
        with open('067_triangle.txt', 'r') as f:
            triangle = build_triangle(f.read())
            self.assertEquals(max_sum_in_path(triangle), 7273)


def build_triangle(data):
    return [[int(n) for n in line.strip().split(' ')] for line in data.strip().split('\n')]


def max_sum_in_path(triangle):
    for i in xrange(len(triangle)-2, -1, -1): # starts from the line before the last one
        for j in xrange(len(triangle[i])):
            triangle[i][j] = max(
                triangle[i][j] + triangle[i+1][j], # left adjacent
                triangle[i][j] + triangle[i+1][j+1] # right adjacent
            )
    return triangle[0][0]
