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
    moves = []

    for tile in board:
        if color == BLACK:
            if board[tile] == BLACK or board[tile] == BLACKKING:
                movesi = Cb.getpossiblemoves(board, tile)
                moves += movesi
        if color == RED:
            if board[tile] == RED or board[tile] == REDKING:
                movesi = Cb.getpossiblemoves(board, tile)
                moves += movesi

    movenum = random.randint(0, moves.count())
    move = moves[movenum]

    return move
