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

