"""
This module puts two AIs against each other in a game and returns the winner.
"""

from CheckerGame.defines import RED, BLACK, REDWON, BLACKWON, NOWIN
import CheckerGame.CheckerBoard as Cb
import AIswitchboard.switchboard as Sb


def duelit(aione, aitwo, turnlimit=100):
    """
    Duels two ais against each other. Returns REDWON, BLACKWON, or NOWIN (draw).

    :param aione: first ai (RED)
    :param aitwo: second ai (BLACK)
    :param turnlimit: if this turn limit is exceeded, the game is announced a draw (NOWIN)
    :return: REDWON, BLACKWON, or NOWIN (draw).
    """
    state = NOWIN
    turn = 1
    board = Cb.getstartingboard()

    if aione not in Sb.SWITCHABLE_AIS or aitwo not in Sb.SWITCHABLE_AIS:
        return NOWIN  # error - should I report this somehow to the caller?

    while (turn < turnlimit):
        # first ai
        fmove = Sb.getaimove(aione, board, RED)
        board = Cb.makemove(board, fmove)
        state = Cb.iswon(board)
        if state != NOWIN:
            break
        # second ai
        smove = Sb.getaimove(aitwo, board, BLACK)
        board = Cb.makemove(board, smove)
        state = Cb.iswon(board)
        if state != NOWIN:
            break

    return state
