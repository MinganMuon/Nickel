"""
Tests for CheckerGame.CheckerBoard
"""

from CheckerGame.defines import *
import CheckerGame.CheckerBoard as Cb

import unittest


# note: I have stopped writing unit tests right now; they are too time consuming when I want to get this off the ground.
#       I may resume them later or do higher-level tests or just do them as I want to make sure something works.
#       Testing code that is simple and I know works is totally redundant and stupid -- I'm not doing it.


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
        # add checks for wins via forced immobility

    def test_getrownumber(self):
        self.assertEqual(Cb.getrownumber(0), 0)
        self.assertEqual(Cb.getrownumber(3), 0)
        self.assertEqual(Cb.getrownumber(5), 1)
        self.assertEqual(Cb.getrownumber(21), 5)
        self.assertEqual(Cb.getrownumber(31), 7)

    def test_getupmoves(self):
        # this does not test filtertype
        sboard = Cb.getstartingboard()
        self.assertEqual(Cb.getupmoves(sboard, 20), [(20, 16, [])]) # left side
        self.assertEqual(Cb.getupmoves(sboard, 22), [(22, 17, []), (22, 18, [])]) # multiple
        self.assertEqual(Cb.getupmoves(sboard, 27), []) # nothing
        self.assertEqual(Cb.getupmoves(sboard, 3), []) # top
        self.assertEqual(Cb.getupmoves(sboard, 19), [(19, 15, [])])  # right side

    def test_getdownmoves(self):
        # this does not test filtertype
        sboard = Cb.getstartingboard()
        self.assertEqual(Cb.getdownmoves(sboard, 4), []) # left side with no right move
        self.assertEqual(Cb.getdownmoves(sboard, 8), [(8, 12, []), (8, 13, [])]) # multiple
        self.assertEqual(Cb.getdownmoves(sboard, 6), [])  # nothing
        self.assertEqual(Cb.getdownmoves(sboard, 26), [])  # nothing again
        self.assertEqual(Cb.getdownmoves(sboard, 30), [])  # bottom
        self.assertEqual(Cb.getdownmoves(sboard, 11), [(11, 15, [])])  # right side

    def test_getpossiblemoves(self):
        # code this maybe?
        pass

    # actually, let's do some testing
    def test_getupjumpmoves(self):
        sboard = Cb.getstartingboard()
        sboard[17] = BLACK
        self.assertEqual(Cb.getupjumpmoves(sboard, 22), [(22, 13, [17])])
        sboard[6] = EMPTY
        self.assertEqual(Cb.getupjumpmoves(sboard, 22), [(22, 6, [17, 9])])
        sboard[18] = BLACK
        self.assertEqual(Cb.getupjumpmoves(sboard, 22), [(22, 6, [17, 9]), (22, 6, [18, 10])])
        # this is fun

    def test_getkingjumpmoves(self):
        sboard = Cb.getstartingboard()
        sboard[22] = REDKING
        sboard[17] = BLACK
        self.assertEqual(Cb.getkingjumpmoves(sboard, 22), [(22, 13, [17])])
        sboard[6] = EMPTY
        self.assertEqual(Cb.getkingjumpmoves(sboard, 22), [(22, 15, [17, 9, 10])])
        sboard[18] = BLACK
        self.assertEqual(Cb.getkingjumpmoves(sboard, 22), [(22, 15, [17, 9, 10]), (22, 13, [18, 10, 9])])
        sboard[22] = EMPTY
        sboard[6] = REDKING
        self.assertEqual(Cb.getkingjumpmoves(sboard, 6), [(6, 15, [9, 17, 18]), (6, 13, [10, 18, 17])])
        # it works! yay!

if __name__ == '__main__':
    unittest.main()
