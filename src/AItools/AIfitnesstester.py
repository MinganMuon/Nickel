"""
Tests the fitness of AIs by putting them against each other for multiple games and then returning the results.
"""

import AItools.AIDueler as AId
from CheckerGame.defines import REDWON, BLACKWON, NOWIN


def getwins(aione, aitwo, numgames):
    """
    Gets the number of wins for each AI over numgames. Each AI will play as both red and black.

    numgames must be even; if it is not it will be increased by one to make it even.

    :param aione: AI number one
    :param aitwo: AI number two
    :param numgames: How many games are we playing?
    :return: tuple: (aionewins, aitwowins, draws)
    """

    if numgames % 2 != 0:  # not even
        numgames += 1

    aionewins = 0
    aitwowins = 0
    draws = 0

    for i in range(numgames//2):  # aione as red
        whowon = AId.duelit(aione, aitwo)
        if whowon == REDWON:
            aionewins += 1
        elif whowon == BLACKWON:
            aitwowins += 1
        else:
            draws += 1

    for i in range(numgames//2):  # aitwo as red
        whowon = AId.duelit(aitwo, aione)
        if whowon == BLACKWON:
            aionewins += 1
        elif whowon == REDWON:
            aitwowins += 1
        else:
            draws += 1

    return (aionewins, aitwowins, draws)
