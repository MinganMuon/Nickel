"""
Provides an UI for the AI fitness tester.
"""

import AItools.AIfitnesstester as AIft
import AIswitchboard.switchboard as AIsb

DRAW_BARGRAPH = True

if __name__ == "__main__":
    possibleais = AIsb.SWITCHABLE_AIS
    print("Possible AIs for testing:")
    print(possibleais)
    aione = possibleais[int(input("Index of AI one: "))]
    aitwo = possibleais[int(input("Index of AI two: "))]
    numgames = int(input("Number of games: "))
    if numgames > 0:
        if aione in possibleais and aitwo in possibleais:
            # let's do this!
            results = AIft.getwins(aione, aitwo, numgames)
            onewin, twowin, draws = results
            print("Number of times that " + aione + " won:")
            print(onewin)
            print("Number of times that " + aitwo + " won:")
            print(twowin)
            print("Number of times that the game resulted in a draw:")
            print(draws)
            if DRAW_BARGRAPH:
                import matplotlib.pyplot as plt
                import numpy as np

                data = [onewin, twowin, draws]
                names = [aione, aitwo, "Draws"]
                x = np.arange(3)

                plt.bar(x, data)
                plt.xticks(x + 0.5, names)  # rotation=90 for vertical labels
                plt.tight_layout()
                plt.show()
