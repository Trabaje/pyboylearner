from instance import GameInstance

import numpy
import sys
import math as maths

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

	def exportstates(self):
		t = []
		for i in range(len(self.games)):
			t.append(self.games[i].exportstates())
		numpy.save("files/states.numpy", t)

	def exportrewards(self):
		t = []
		for i in range(len(self.games)):
			t.append(self.games[i].exportrewards())
		numpy.save("files/rewards.numpy", t)


	
	def printscreen(self):
		screenstring = ''
		count = len(self.games)
		perrow = maths.ceil(maths.sqrt(count))
		rows = maths.ceil(count/perrow)
		t = []
		dims = []
		for i in range(rows):
			r = []
			for j in range(perrow):
				k = i * perrow + j
				if k < count:
					r.append(self.games[k].screen(perrow))
					if len(dims) == 0:
						dims = r[0].shape
				else:
					r.append(numpy.zeros(dims, dtype=int))
					#r.append(self.games[0].screen(perrow))
			t.append(numpy.concatenate(r, axis = 1))
		tempscreen = numpy.concatenate(t, axis = 0)
		
		#r1 = numpy.concatenate([self.games[0].screen(2), self.games[1].screen(2)], axis = 1)
		#r2 = numpy.concatenate([self.games[2].screen(2), self.games[3].screen(2)], axis = 1)
		#tempscreen = numpy.concatenate([r1, r2], axis = 0)
		
		#tempscreen = self.games[0].screen(2)
		#tempscreen = numpy.concatenate([tempscreen, tempscreen], axis=1)
		#tempscreen = numpy.concatenate([tempscreen, tempscreen], axis = 0)
		for i in range(tempscreen.shape[0]):
			for j in range(tempscreen.shape[1]):
				screenstring += '\033[48;2;' + str(tempscreen[i,j,0]) + ';' +  str(tempscreen[i,j,1]) + ';' +  str(tempscreen[i,j,2]) + 'm '
				#x = 1
			screenstring += '\033[0m\n'
		
		refresh = ''
		if self.screenprinted == 1:
			#print(str(screenstring.count('\n')+1))
			for _ in range(screenstring.count('\n')+1):
				refresh += '\033[A'
				#x=1
		
		print(refresh + screenstring)
		sys.stdout.flush()
		self.screenprinted = 1
		
