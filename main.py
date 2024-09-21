import sys
import numpy

from instance import GameInstance

numpy.set_printoptions(threshold=sys.maxsize)

screenprinted = 0

game = GameInstance()

def printscreen():
	global screenprinted, name, screenhistory
	screenstring = ''
	tempscreen = game.screen(2)
	for i in range(tempscreen.shape[0]):
		for j in range(tempscreen.shape[1]):
			screenstring += '\033[48;2;' + str(tempscreen[i,j,0]) + ';' +  str(tempscreen[i,j,1]) + ';' +  str(tempscreen[i,j,2]) + 'm '
			x = 1
		screenstring += '\033[0m\n'

	
	refresh = ''
	if screenprinted == 1:
		for _ in range(screenstring.count('\n')+1):
			refresh += '\033[A'

	print(refresh + screenstring)
	sys.stdout.flush()
	screenprinted = 1

for _ in range(50):
	game.tick()
	printscreen()

game.stop()

#numpy.savetxt("scores.csv", finalisedrewards, delimiter=",")
