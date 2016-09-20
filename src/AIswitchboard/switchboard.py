"""
AI switchboard code.
"""

import RandomAI.RandomAI

# this is a list of the AIs that can be called through the AIswitchboard
SWITCHABLE_AIS = ['RandomAI']


def getaimove(ai, board, color):
    """
    Gets a move from ai for color on board.

    :param ai: name of AI, must be in SWITCHABLE_AIS
    :param board: 32-element list
    :param color: what color is the AI moving for?
    :return: move: (starting tile, ending tile, list of jumped tiles)
    """
    if ai in SWITCHABLE_AIS:
        if ai == 'RandomAI':
            return RandomAI.RandomAI.getrandomaimove(board, color)
        else:
            # whoops! something wasn't coded right
            return []
    else:
        return []
