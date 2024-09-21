import numpy
import sys

from manager import ConsoleManager

numpy.set_printoptions(threshold=sys.maxsize)

games = ConsoleManager(2)

for _ in range(50):
	games.tick()
	games.printscreen()

games.stop()

#numpy.savetxt("scores.csv", finalisedrewards, delimiter=",")
