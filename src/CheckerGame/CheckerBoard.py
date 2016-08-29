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
