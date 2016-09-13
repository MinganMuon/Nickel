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
    if (board.count(RED) + board.count(REDKING)) == 0:  # black wins
        won = BLACKWON
    elif (board.count(BLACK) + board.count(BLACKKING)) == 0:  # red wins
        won = REDWON
    # if no moves are possible for a color, the other color wins
    elif not getallpossiblemoves(board, RED):  # black wins
        won = BLACKWON
    elif not getallpossiblemoves(board, BLACK):  # red wins
        won = REDWON
    return won

# helper functions for getpossiblemoves

def getrownumber(tile):
    """
    Helper function that returns the 0-indexed row number of a tile.

    :param tile: tile number, 0-indexed
    :return: 0-indexed row number of tile
    """
    return (int)(tile/4)


def getleftup(tile):
    """
    Gets the tile left and up of tile. If an invalid tile number results, return -1.

    :param tile:  tile number (position in board, 0-indexed)
    :return: tile left and up of tile; if not possible, returns -1
    """

    newtile = -1

    rownumber = getrownumber(tile)
    oddrn = rownumber % 2

    if (tile not in toptiles) and (tile not in lefttiles):  # left and up
        if oddrn:
            newtile = tile - 5
        else:
            newtile = tile - 4

    return newtile


def getrightup(tile):
    """
    Gets the tile right and up of tile. If an invalid tile number results, return -1.

    :param tile:  tile number (position in board, 0-indexed)
    :return: tile right and up of tile; if not possible, returns -1
    """

    newtile = -1

    rownumber = getrownumber(tile)
    oddrn = rownumber % 2

    if (tile not in toptiles) and (tile not in righttiles):  # right and up
        if oddrn:
            newtile = tile - 4
        else:
            newtile = tile - 3

    return newtile


def getleftdown(tile):
    """
    Gets the tile left and down of tile. If an invalid tile number results, return -1.

    :param tile:  tile number (position in board, 0-indexed)
    :return: tile left and down of tile; if not possible, returns -1
    """

    newtile = -1

    rownumber = getrownumber(tile)
    oddrn = rownumber % 2

    if (tile not in bottomtiles) and (tile not in lefttiles):  # left and down
        if oddrn:
            newtile = tile + 3
        else:
            newtile = tile + 4

    return newtile


def getrightdown(tile):
    """
    Gets the tile right and down of tile. If an invalid tile number results, return -1.

    :param tile:  tile number (position in board, 0-indexed)
    :return: tile right and down of tile; if not possible, returns -1
    """

    newtile = -1

    rownumber = getrownumber(tile)
    oddrn = rownumber % 2

    if (tile not in bottomtiles) and (tile not in righttiles):  # right and down
        if oddrn:
            newtile = tile + 4
        else:
            newtile = tile + 5

    return newtile


def getupmoves(board, tile, filtertype=EMPTY):
    """
    Gets a list of possible non-jump up moves the tile can move.

    filtertype can be used to filter the up moves by a tile type other than EMPTY.

    :param board: 32-element list
    :param tile: tile number (position in board, 0-indexed)
    :param filtertype: the tile type that the tile in question is checked against
    :return: list of tuples - (starting tile, ending tile, list of jumped tiles)
    """

    rlist = []

    # left move
    leftup = getleftup(tile)
    if leftup != -1:
        if board[leftup] == filtertype:
            rlist.append((tile, leftup, []))
    # right move
    rightup = getrightup(tile)
    if rightup != -1:
        if board[rightup] == filtertype:
            rlist.append((tile, rightup, []))

    return rlist


def getdownmoves(board, tile, filtertype=EMPTY):
    """
    Gets a list of possible non-jump down moves the tile can move.

    filtertype can be used to filter the down moves by a tile type other than EMPTY.

    :param board: 32-element list
    :param tile: tile number (position in board, 0-indexed)
    :param filtertype: the tile type that the tile in question is checked against
    :return: list of tuples - (starting tile, ending tile, list of jumped tiles)
    """

    rlist = []

    # left move
    leftdown = getleftdown(tile)
    if leftdown != -1:
        if board[leftdown] == filtertype:
            rlist.append((tile, leftdown, []))
    # right move
    rightdown = getrightdown(tile)
    if rightdown != -1:
        if board[rightdown] == filtertype:
            rlist.append((tile, rightdown, []))

    return rlist


def getupjumpmoves(board, tile, filtertype=(BLACK, BLACKKING), rc=3):
    """
    Gets the possible up jump moves that a tile can take.

    filtertype can be used to filter the possible jump tiles by a tile type other than the default.

    :param board: 32-element list
    :param tile: tile number (position in board, 0-indexed)
    :param filtertype: tuple: the tile type(s) that the tile in question can jump
    :param rc: recursion counter, used to limit recursion.
            On the calling side, set this to how deep it will search for jumps.
    :return: list of tuples - (starting tile, ending tile, list of jumped tiles)
    """
    iboard = board[:]
    rlist = []

    if rc == 0:  # limit recursion
        return []

    # left up jump
    lu = getleftup(tile)
    if lu != -1:
        if iboard[lu] in filtertype:
            luf = getleftup(lu)
            if luf != -1:
                if iboard[luf] == EMPTY:
                    rlist.append((tile, luf, [lu]))

    # right up jump
    ru = getrightup(tile)
    if ru != -1:
        if iboard[ru] in filtertype:
            ruf = getrightup(ru)
            if ruf != -1:
                if iboard[ruf] == EMPTY:
                    rlist.append((tile, ruf, [ru]))

    for i, ritem in enumerate(rlist):
        glist = getupjumpmoves(makemove(iboard, ritem), ritem[1], filtertype, rc - 1)
        for gst, get, gjt in glist:
            rlist[i] = (ritem[0], get, ritem[2] + gjt)

    return rlist


def getdownjumpmoves(board, tile, filtertype=(RED, REDKING), rc=3):
    """
    Gets the possible down jump moves that a tile can take.

    filtertype can be used to filter the possible jump tiles by a tile type other than the default.

    :param board: 32-element list
    :param tile: tile number (position in board, 0-indexed)
    :param filtertype: tuple: the tile type(s) that the tile in question can jump
    :param rc: recursion counter, used to limit recursion.
            On the calling side, set this to how deep it will search for jumps.
    :return: list of tuples - (starting tile, ending tile, list of jumped tiles)
    """
    iboard = board[:]
    rlist = []

    if rc == 0:  # limit recursion
        return []

    # left down jump
    lu = getleftdown(tile)
    if lu != -1:
        if iboard[lu] in filtertype:
            luf = getleftdown(lu)
            if luf != -1:
                if iboard[luf] == EMPTY:
                    rlist.append((tile, luf, [lu]))

    # right down jump
    ru = getrightdown(tile)
    if ru != -1:
        if iboard[ru] in filtertype:
            ruf = getrightdown(ru)
            if ruf != -1:
                if iboard[ruf] == EMPTY:
                    rlist.append((tile, ruf, [ru]))

    for i, ritem in enumerate(rlist):
        glist = getdownjumpmoves(makemove(iboard, ritem), ritem[1], filtertype, rc - 1)
        for gst, get, gjt in glist:
            rlist[i] = (ritem[0], get, ritem[2] + gjt)

    return rlist


def getkingjumpmoves(board, tile, rc=3):
    """
    Gets the possible jump moves that a king can take.

    :param board: 32-element list
    :param tile: tile number (position in board, 0-indexed)
    :param rc: recursion counter, used to limit recursion.
            On the calling side, set this to how deep it will search for jumps.
    :return: list of tuples - (starting tile, ending tile, list of jumped tiles)
    """
    iboard = board[:]
    rlist = []
    if board[tile] == REDKING:
        filtertype = (BLACK, BLACKKING)
    elif board[tile] == BLACKKING:
        filtertype = (RED, REDKING)
    else:
        # tile is not a king
        return []

    if rc == 0:  # limit recursion
        return []

    rlist += getdownjumpmoves(iboard, tile, filtertype, rc=1)
    rlist += getupjumpmoves(iboard, tile, filtertype, rc=1)

    for i, ritem in enumerate(rlist):
        glist = getkingjumpmoves(makemove(iboard, ritem), ritem[1], rc - 1)
        for gst, get, gjt in glist:
            rlist[i] = (ritem[0], get, ritem[2] + gjt)

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

    # get jump moves
    # red
    if board[tile] == RED:
        jlist = getupjumpmoves(board, tile)
        if jlist:
            return jlist  # tile has to jump
    # black
    if board[tile] == BLACK:
        jlist = getdownjumpmoves(board, tile)
        if jlist:
            return jlist  # tile has to jump
    # red king
    if board[tile] == REDKING:
        jlist = getkingjumpmoves(board, tile)
        if jlist:
            return jlist  # tile has to jump
    # black king
    if board[tile] == BLACKKING:
        jlist = getkingjumpmoves(board, tile)
        if jlist:
            return jlist  # tile has to jump

    # get non-jump moves
    # red is going up
    if board[tile] == RED or board[tile] == BLACKKING or board[tile] == REDKING:
        rlist += getupmoves(board, tile)
    if board[tile] == BLACK or board[tile] == REDKING or board[tile] == BLACKKING:
        rlist += getdownmoves(board, tile)

    return rlist


def getallpossiblemoves(board, color):
    """
    Gets all possible moves for every tile on the board.

    :param board: 32-element list
    :param color: what color are we getting moves for?
    :return: list of tuples - (starting tile, ending tile, list of jumped tiles)
    """
    moves = []

    for tile, tiletype in enumerate(board):
        if color == BLACK:
            if tiletype == BLACK or tiletype == BLACKKING:
                moves += getpossiblemoves(board, tile)
        if color == RED:
            if tiletype == RED or tiletype == REDKING:
                moves += getpossiblemoves(board, tile)

    result = []
    onlyjump = False
    if len(moves) != 0:  # now delete non-jump moves if needed
        for move in moves:
            if move[2]:
                onlyjump = True
                result.append(move)

    if onlyjump:
        return result
    else:
        return moves


def iskingable(board, tile):
    """
    Determines if a tile is kingable.

    :param tile: 0-indexed tile number
    :return: bool: true if tile is kingable
    """
    if tile in bottomtiles:
        if board[tile] == BLACK:
            return True
    elif tile in toptiles:
        if board[tile] == RED:
            return True
    else:
        return False


def makemove(board, move):
    """
    Makes a move on a board. Kings the tile if needed

    :param board: 32-element list
    :param move: [starting tile, ending tile, list of jumped tiles]
    :return: the modified board (32-element list)
    """
    iboard = board[:]
    if move:
        st, et, jt = move[0], move[1], move[2]
        iboard[et] = iboard[st]
        iboard[st] = EMPTY
        for tile in jt:
            iboard[tile] = EMPTY
        if iskingable(iboard, et):
            if iboard[et] == RED:
                iboard[et] = REDKING
            elif iboard[et] == BLACK:
                iboard[et] = BLACKKING

    return iboard
