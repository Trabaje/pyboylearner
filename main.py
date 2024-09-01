from pyboy import PyBoy

import sys
import numpy

numpy.set_printoptions(threshold=sys.maxsize)

screenprinted = 0

def printscreen():
	global screenprinted
	refresh = '\033[A'
	screenstring = ''
	for i in range(pyboy.screen.ndarray.shape[0]):
		for j in range(pyboy.screen.ndarray.shape[1]):
			screenstring += '\033[48;2;' + str(pyboy.screen.ndarray[i,j,0]) + ';' +  str(pyboy.screen.ndarray[i,j,1]) + ';' +  str(pyboy.screen.ndarray[i,j,2]) + 'm '
		if screenprinted == 1:
			refresh += '\033[A'
		screenstring += '\033[0m\n'
	print(refresh + screenstring)
	sys.stdout.flush()
	screenprinted = 1

pyboy = PyBoy('files/rom.gb')
for _ in range(100):
	pyboy.tick()
	printscreen()
#	print(pyboy.screen.ndarray[:,:,0], end='\r')
pyboy.stop()
