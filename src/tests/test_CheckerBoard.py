"""
Tests for CheckerGame.CheckerBoard
"""

from CheckerGame.defines import *
import CheckerGame.CheckerBoard as Cb

import unittest


class TestCheckerBoard(unittest.TestCase):

    def test_getemptyboard(self):
        board = Cb.getemptyboard()
        self.assertEqual(len(board), 32)  # size of board
        self.assertEqual(board.count(EMPTY), 32)  # number of empty tiles

    def test_getstartingboard(self):
        board = Cb.getstartingboard()
        self.assertEqual(len(board), 32)  # size of board
        self.assertEqual(board.count(BLACK), 12)  # number of black tiles
        self.assertEqual(board.count(EMPTY), 8)  # number of empty tiles
        self.assertEqual(board.count(RED), 12)  # number of red tiles


if __name__ == '__main__':
    unittest.main()
