"""
A simple random AI. It gets all the possible moves it can make and selects one at random.
"""

import CheckerGame.CheckerBoard as Cb
from CheckerGame.defines import BLACK, RED, REDKING, BLACKKING
import random


def getrandomaimove(board, color=BLACK):
    """
    Gets a random move.

    :param board: 32-element list
    :param color: what color is the AI getting a move for?
    :return: list: [starting tile, ending tile, (tiles jumped)]
    """

    moves = Cb.getallpossiblemoves(board, color)

    if (len(moves) != 0):
        movenum = random.randint(0, len(moves) - 1)
        move = moves[movenum]
        return move
    else:
        return []
