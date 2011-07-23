# coding: utf8

import unittest

class TestCoinPossibilities(unittest.TestCase):

    def setUp(self):
        self.coins = (1, 2, 5, 10, 20, 50, 100, 200)

    def test_coin_possibilities_for_1p(self):
        assert 1 == coin_possibilities(1, self.coins)

    def test_coin_possibilities_for_2p(self):
        assert 2 == coin_possibilities(2, self.coins)

    def test_coin_possibilities_for_3p(self):
        assert 2 == coin_possibilities(3, self.coins)

    def test_coin_possibilities_for_4p(self):
        assert 3 == coin_possibilities(4, self.coins)

    def test_coin_possibilities_for_5p(self):
        assert 4 == coin_possibilities(5, self.coins)

    def test_coin_possibilities_for_10p(self):
        assert 11 == coin_possibilities(10, self.coins)

    def test_coin_possibilities_for_50p(self):
        assert 451 == coin_possibilities(50, self.coins)

    def test_coin_possibilities_for_100p(self):
        assert 4563 == coin_possibilities(100, self.coins)

    def test_coin_possibilities_for_200p(self):
        assert 73682 == coin_possibilities(200, self.coins)


def recursive_coin_possibilities(value, current_value, coins, coin_index):
    if coin_index < 0:
        return 0
    current_coin = coins[coin_index]
    max_number_of_coins = (value - current_value)/current_coin
    possibilities = 0
    for coeficient in range(max_number_of_coins + 1):
        possible_value = current_value + coeficient * current_coin
        if possible_value == value:
            possibilities += 1
        else:
            possibilities += recursive_coin_possibilities(value, possible_value, coins, coin_index - 1)
    return possibilities


def coin_possibilities(value, coins):
    possibilities = recursive_coin_possibilities(value, 0, coins, len(coins)-1)
    return possibilities
