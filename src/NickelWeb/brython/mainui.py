from browser import document as doc
from browser import svg
from browser import alert
from browser import ajax
from browser import html
from browser import timer
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


def gettilenumber(row, col):
    """
    Gets the tile number for the tile with the specified row and col numbers.

    :param row: row (0-indexed)
    :param col: col (0-indexed)
    :return: tile number, 0-indexed
    """

    even = row % 2 # 1 if even
    tile = row * 4
    col += 1
    if even == 1:
        col += 1
        tile += col/2
    else:
        col += 2
        tile += col/2

    # get it to a int
    if tile.is_integer():
        tile = int(tile)
    else:
        # something is wrong; the given row, col do not specify a valid tile position...
        return 'error' # I should, like, do valid error checking

    if even == 1:
        return tile - 1
    else:
        return tile - 2


def printboard(board):
    """
    Prints the gameboard on the screen.

    :param board: 32-element list
    :return: nothing
    """
    panel = doc['panel2']

    # delete previously drawn circles
    panel.clear()

    # draw new ones
    for tile, tiletype in enumerate(board):
        if tiletype != EMPTY:
            # here goes repetition again...
            if tiletype == RED:
                scircle = svg.circle(cx=(getcolnumber(tile)*64 + 32), cy=(getrownumber(tile)*64 + 32),
                                     r=32, fill="red")  # +32 for radius offset
                scircle.setAttributeNS(None, 'pointer-events', 'none')
                panel <= scircle
            elif tiletype == REDKING:
                scircle = svg.circle(cx=(getcolnumber(tile)*64 + 32), cy=(getrownumber(tile)*64 + 32),
                                     r=32, fill="red", stroke="orange", stroke_width=5)  # +32 for radius offset
                scircle.setAttributeNS(None, 'pointer-events', 'none')
                panel <= scircle
            if tiletype == BLACK:
                scircle = svg.circle(cx=(getcolnumber(tile)*64 + 32), cy=(getrownumber(tile)*64 + 32),
                                     r=32, fill="black")  # +32 for radius offset
                scircle.setAttributeNS(None, 'pointer-events', 'none')
                panel <= scircle
            elif tiletype == BLACKKING:
                scircle = svg.circle(cx=(getcolnumber(tile)*64 + 32), cy=(getrownumber(tile)*64 + 32),
                                     r=32, fill="black", stroke="orange", stroke_width=5)  # +32 for radius offset
                scircle.setAttributeNS(None, 'pointer-events', 'none')
                panel <= scircle


def getgsb():
    """
    Makes an AJAX call to get the starting board

    :return: 32-element list
    """
    req = ajax.ajax()
    req.open('GET', 'gsb', False)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()
    return json.loads(req.text)


def getiswon(board):
    """
    Makes an AJAX call to determine whether the game has been won.

    :param board: 32-element list
    :return: NOWIN, REDWIN, or BLACKWIN
    """
    req = ajax.ajax()
    req.open('get', 'iswon/' + "?board=%s" % json.dumps(board), False)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()
    return json.loads(req.text)


def getgpmoves(board, tile):
    """
    Makes an AJAX call to determine the possible moves a tile can make.

    :param board: 32-element list
    :param tile: tile number (position in board, 0-indexed)
    :return: list of lists (tuples?) - [starting tile, ending tile, list of jumped tiles]
    """
    req = ajax.ajax()
    req.open('get', 'gpmoves/' + "?board=%s&tile=%s" % (json.dumps(board), tile), False)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()
    return json.loads(req.text)


def getgraim(board, color=BLACK):
    """
    Makes an AJAX call to get a move from RandomAI

    :param board: 32-element list
    :param color: what color is the AI playing as?
    :return: move: [starting tile, ending tile, list of jumped tiles]
    """
    req = ajax.ajax()
    req.open('get', 'getrandomaimove/' + "?board=%s&color=%s" % (json.dumps(board), json.dumps(color)), False)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()
    return json.loads(req.text)


def makemove(board, move):
    """
    Makes a move on a board.

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
    return iboard

# I HATE having to make these global
redsturn = True
cboard = []
selectedtile = -1
ai = ""
whowon = NOWIN
glt = None

def cbclick(ev):
    global selectedtile, cboard, redsturn

    if cboard:
        if redsturn:
            row = int(ev.clientY / 64) - 1
            col = int(ev.clientX / 64)
            tile = gettilenumber(row, col)
            if tile == 'error':
                alert(tile)
                return
            #alert(tile)
            if tile == selectedtile:
                # unhighlight selected tile
                doc['panel2'].remove(doc['panel2'].children[-1])
                selectedtile = -1
            elif selectedtile == -1:
                if cboard[tile] == RED or cboard[tile] == REDKING:
                    selectedtile = tile
                    # highlight selected tile
                    scircle = svg.rect(x=(getcolnumber(tile) * 64), y=(getrownumber(tile) * 64),
                                         width=64, height=64, stroke='orange', stroke_width=3, fill_opacity=0)
                    scircle.setAttributeNS(None, 'pointer-events', 'none')
                    doc['panel2'] <= scircle
            elif selectedtile != -1 and tile != selectedtile:
                moves = getgpmoves(cboard, selectedtile)
                for move in moves:
                    if move[0] == selectedtile and move[1] == tile:
                        # unhighlight selected tile
                        doc['panel2'].remove(doc['panel2'].children[-1])
                        selectedtile = -1
                        cboard = makemove(cboard, move)
                        alert(move)
                        # print board
                        printboard(cboard)
                        redsturn = False
                        return


def gameloop():
        global cboard, redsturn, selectedtile, ai, whowon, glt

        if not redsturn:
            # has the game been won?
            whowon = getiswon(cboard)
            if whowon == NOWIN:
                if ai == 'RandomAI':  # do some error checking here?
                    move = getgraim(cboard, BLACK)
                    alert(move)
                    cboard = makemove(cboard, move)
                    # print board
                    printboard(cboard)
                redsturn = True
                # has the game been won?
                whowon = getiswon(cboard)

        if whowon == REDWON:
            alert("Red won!")
            redsturn = False  # user can't move after a win
            timer.clearinterval(glt)
        elif whowon == BLACKWON:
            alert("Black won!")
            redsturn = False  # user can't move after a win
            timer.clearinterval(glt)


def newgame(ev):
    global cboard, redsturn, selectedtile, ai, glt

    alert("Starting new game with " + doc["aiselect"].value + " as AI!")

    whowon = NOWIN
    cboard = getgsb()
    printboard(cboard)
    redsturn = True
    ai = doc["aiselect"].value
    # game loop
    glt = timer.set_interval(gameloop, 20)


doc["play"].bind('click', newgame)
doc["svgp"].bind('click', cbclick)

choices = ['RandomAI']
for item in choices:
    doc["aiselect"] <= html.OPTION(item)
