"""
The CheckerBoard module contains the code for creating, analyzing, and manipulating checker boards.
"""

from CheckerGame.defines import *


def getemptyboard():
    """
    Gets an empty checkerboard in 32-element list form.

    :return: 32-element list
    """
    return [EMPTY for x in range(32)]


def getstartingboard():
    """
    Gets the starting checkerboard in 32-element list form. Black is on the top (first elements).

    :return: 32-element list
    """
    outboard = []
    for i in range(12):
        outboard.append(BLACK)
    for i in range(8):
        outboard.append(EMPTY)
    for i in range(12):
        outboard.append(RED)
    return outboard

def iswon(board):
    """
    Determines if the board represents a winning position.

    :param board: 32-element list
    :return: BLACKWON, REDWON, or NOWIN
    """
    won = NOWIN
    if board.count(RED) == 0:  # black wins
        won = BLACKWON
    elif board.count(BLACK) == 0:  # red wins
        won = REDWON
    # todo: if no moves are possible for a color, the other color wins
    return won

