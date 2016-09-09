from browser import document as doc
from browser import alert


def newgame(ev):
    alert("Starting new game with " + doc["aiselect"].title + "as AI!")

doc["play"].bind('click', newgame)
