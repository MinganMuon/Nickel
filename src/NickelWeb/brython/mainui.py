from browser import document as doc
from browser import alert


def lala(ev):
    alert("Hello!")
    doc["echo"].text = "ha"

doc["echo"].bind('click', lala)
