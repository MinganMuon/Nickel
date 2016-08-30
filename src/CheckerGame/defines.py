"""
The defines files defines stuff needed in the various CheckerGame modules.
Other packages can safely import this to interface with the CheckerGame modules.
"""


# defines
BLACK = 'black'
RED = 'red'
REDKING = 'redking'
BLACKKING = 'blackking'
EMPTY = 'empty'
INVALID = 'invalid'

BLACKWON = 'blackwon'
REDWON = 'redwon'
NOWIN = 'nowin'

# what tiles are on the ends?
lefttiles = (4, 12, 20, 28)
righttiles = (3, 11, 19, 27)
toptiles = (0, 1, 2, 3)
bottomtiles = (28, 29, 30, 31)
