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

    def test_iswon(self):
        sboard = Cb.getstartingboard() # no win
        rboard = Cb.getemptyboard()
        bboard = Cb.getemptyboard()
        rboard[0] = RED # red win
        bboard[0] = BLACK # black win
        self.assertEqual(Cb.iswon(sboard), NOWIN) # checks
        self.assertEqual(Cb.iswon(rboard), REDWON)
        self.assertEqual(Cb.iswon(bboard), BLACKWON)
        # todo: add checks for wins via forced immobility

    def test_getrownumber(self):
        self.assertEqual(Cb.getrownumber(0), 0)
        self.assertEqual(Cb.getrownumber(3), 0)
        self.assertEqual(Cb.getrownumber(5), 1)
        self.assertEqual(Cb.getrownumber(21), 5)
        self.assertEqual(Cb.getrownumber(31), 7)

    def test_getupmoves(self):
        sboard = Cb.getstartingboard()
        self.assertEqual(Cb.getupmoves(sboard, 20), [(20, 16, [])]) # left side
        self.assertEqual(Cb.getupmoves(sboard, 22), [(22, 17, []), (22, 18, [])]) # multiple
        self.assertEqual(Cb.getupmoves(sboard, 27), []) # nothing
        self.assertEqual(Cb.getupmoves(sboard, 3), []) # top
        self.assertEqual(Cb.getupmoves(sboard, 19), [(19, 15, [])])  # right side

    def test_getdownmoves(self):
        sboard = Cb.getstartingboard()
        self.assertEqual(Cb.getdownmoves(sboard, 4), []) # left side with no right move
        self.assertEqual(Cb.getdownmoves(sboard, 8), [(8, 12, []), (8, 13, [])]) # multiple
        self.assertEqual(Cb.getdownmoves(sboard, 6), [])  # nothing
        self.assertEqual(Cb.getdownmoves(sboard, 26), [])  # nothing again
        self.assertEqual(Cb.getdownmoves(sboard, 30), [])  # bottom
        self.assertEqual(Cb.getdownmoves(sboard, 11), [(11, 15, [])])  # right side


if __name__ == '__main__':
    unittest.main()
