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

# helper functions for getpossiblemoves

def getrownumber(tile):
    """
    Helper function that returns the 0-indexed row number of a tile.

    :param tile: tile number, 0-indexed
    :return: 0-indexed row number of tile
    """
    return (int)(tile/4)


def getupmoves(board, tile, filtertype=EMPTY):
    """
    Gets a list of possible non-jump up moves the tile can move.

    filtertype can be used to filter the up moves by a tile type other than EMPTY;
    for example, to determine if any tiles could be jumped by a piece.

    :param board: 32-element list
    :param tile: tile number (position in board, 0-indexed)
    :param filtertype: the tile type that the tile in question is checked against
    :return: list of tuples - (starting tile, ending tile, list of jumped tiles)
    """

    rlist = []

    # this is somewhat hackish of a solution
    rownumber = getrownumber(tile)
    oddrn = rownumber % 2
    if (tile not in toptiles) and (tile not in lefttiles):  # left move
        if oddrn:
            if board[tile - 5] == filtertype:
                rlist.append((tile, tile - 5, []))
        else:
            if board[tile - 4] == filtertype:
                rlist.append((tile, tile - 4, []))
    if (tile not in toptiles) and (tile not in righttiles):  # right move
        if oddrn:
            if board[tile - 4] == filtertype:
                rlist.append((tile, tile - 4, []))
        else:
            if board[tile - 3] == filtertype:
                rlist.append((tile, tile - 3, []))

    return rlist


def getdownmoves(board, tile, filtertype=EMPTY):
    """
    Gets a list of possible non-jump down moves the tile can move.

    filtertype can be used to filter the down moves by a tile type other than EMPTY;
    for example, to determine if any tiles could be jumped by a piece.

    :param board: 32-element list
    :param tile: tile number (position in board, 0-indexed)
    :param filtertype: the tile type that the tile in question is checked against
    :return: list of tuples - (starting tile, ending tile, list of jumped tiles)
    """

    rlist = []

    # this is somewhat hackish of a solution
    rownumber = getrownumber(tile)
    oddrn = rownumber % 2
    if (tile not in bottomtiles) and (tile not in lefttiles):  # left move
        if oddrn:
            if board[tile + 3] == filtertype:
                rlist.append((tile, tile + 3, []))
        else:
            if board[tile + 4] == filtertype:
                rlist.append((tile, tile + 4, []))
    if (tile not in bottomtiles) and (tile not in righttiles):  # right move
        if oddrn:
            if board[tile + 4] == filtertype:
                rlist.append((tile, tile + 4, []))
        else:
            if board[tile + 5] == filtertype:
                rlist.append((tile, tile + 5, []))

    return rlist

# end helper functions

def getpossiblemoves(board, tile):
    """
    Gets the possible moves for the specified tile number on the specified board.

    :param board: 32-element list
    :param tile: tile number (position in board, 0-indexed)
    :return: list of tuples - (starting tile, ending tile, list of jumped tiles)
    """

    # return list
    rlist = []

    # get non-jump moves
