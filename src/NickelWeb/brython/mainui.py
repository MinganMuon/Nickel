from browser import document as doc
from browser import svg
from browser import alert
from browser import ajax
import json

# defines, taken from CheckerGame/defines.py
# I hate copy-pasting but I don't see a way around it, brython being client-side and checkergame being server-side
BLACK = 'black'
RED = 'red'
REDKING = 'redking'
BLACKKING = 'blackking'
EMPTY = 'empty'
INVALID = 'invalid'
BLACKWON = 'blackwon'
REDWON = 'redwon'
NOWIN = 'nowin'


def getrownumber(tile):
    """
    Helper function that returns the 0-indexed row number of a tile.

    Taken from CheckerBoard.py.

    :param tile: tile number, 0-indexed
    :return: 0-indexed row number of tile
    """
    return int(tile/4)


def getcolnumber(tile):
    """
    Helper function that returns the 0-indexed column number of a tile.

    :param tile: tile number, 0-indexed
    :return: 0-indexed column number of tile
    """
    even = int(tile/4) % 2  # 1 if even
    if even == 1:
        x = (tile - (int(tile/4))*4)*2
    else:
        x = (tile - (int(tile/4))*4)*2 + 1
    return x


def printboard(board):
    """
    Prints the gameboard on the screen.

    :param board: 32-element list
    :return: nothing
    """
    panel = doc['panel']
    for tile, tiletype in enumerate(board):
        if tiletype != EMPTY:
            # here goes repetition again...
            if tiletype == RED:
                scircle = svg.circle(cx=(getcolnumber(tile)*64 + 32), cy=(getrownumber(tile)*64 + 32),
                                     r=32, fill="red")  # +32 for radius offset
                panel <= scircle
            elif tiletype == REDKING:
                scircle = svg.circle(cx=(getcolnumber(tile)*64 + 32), cy=(getrownumber(tile)*64 + 32),
                                     r=32, fill="red", stroke="orange", stroke_width=5)  # +32 for radius offset
                panel <= scircle
            if tiletype == BLACK:
                scircle = svg.circle(cx=(getcolnumber(tile)*64 + 32), cy=(getrownumber(tile)*64 + 32),
                                     r=32, fill="black")  # +32 for radius offset
                panel <= scircle
            elif tiletype == BLACKKING:
                scircle = svg.circle(cx=(getcolnumber(tile)*64 + 32), cy=(getrownumber(tile)*64 + 32),
                                     r=32, fill="black", stroke="orange", stroke_width=5)  # +32 for radius offset
                panel <= scircle


def newgame(ev):
    alert("Starting new game with " + doc["aiselect"].title + "as AI!")

    req = ajax.ajax()
    req.open('GET', 'gsb', False)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()
    alert(json.loads(req.text))

    printboard(json.loads(req.text))

doc["play"].bind('click', newgame)
