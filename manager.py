from instance import GameInstance

import numpy
import sys


class ConsoleManager:

	def __init__(self, num = 1, rom = 'files/rom.gbc'):
		
		self.screenprinted = 0
		
		self.games = []
		
		for i in range(num):
			self.games.append(GameInstance())
	
	def tick(self, num = 1):
		for i in range(len(self.games)):
			self.games[i].tick(num)
	
	def stop(self):
		for i in range(len(self.games)):
			self.games[i].stop()
	
	def printscreen(self):
		screenstring = ''
		tempscreen = self.games[0].screen(2)
		for i in range(tempscreen.shape[0]):
			for j in range(tempscreen.shape[1]):
				screenstring += '\033[48;2;' + str(tempscreen[i,j,0]) + ';' +  str(tempscreen[i,j,1]) + ';' +  str(tempscreen[i,j,2]) + 'm '
				#x = 1
			screenstring += '\033[0m\n'
		
		refresh = ''
		if self.screenprinted == 1:
			for _ in range(screenstring.count('\n')+1):
				refresh += '\033[A'
	
		print(refresh + screenstring)
		sys.stdout.flush()
		screenprinted = 1
		