from pyboy import PyBoy

import numpy
import random

class GameInstance:
	
	def __init__(self, rom = 'files/rom.gbc', acc= 10):
		self.pyboy = PyBoy(rom)
		self.pyboy.set_emulation_speed(0)
		
		self.oldscore = 0
		self.accumulate  = acc
		
		self.name = [' ']
		self.inputs = {
			"up": 0.0,
			"down": 0.0,
			"left": 0.0, 
			"right": 0.0,
			"b": 0.0,
			"a": 0.0,
			"select": 0.0,
			"start": 0.0
		}
		self.highestinput = ""
		
		self.screenhistory = []
		self.accumulatingrewards = []
		self.statestore = []
		self.finalisedrewards = []
		self.finalisedstates = []
	
	def screen(self, step = 1):
		return self.pyboy.screen.ndarray[::step, ::step]
	
	
	def memory_sweep(self):
		self.name = ''.join(str(x) for x in self.pyboy.memory[0xD47D:0xD486])
		self.new_screen_check()
		self.statesandscores()
	
	def generate_inputs(self):
		self.inputs.update( {
			"up": random.uniform(0,1),
			"down": random.uniform(0,1),
			"left" : random.uniform(0,1),
			"right": random.uniform(0,1),
			"b": random.uniform(0,1),
			"a" : random.uniform(0,1),
			"select": random.uniform(0,1),
			"start": random.uniform(0,1)
		} )
		self.highestinput = max(self.inputs, key = self.inputs.get)
		self.statestore.append(self.gatherstate())
	
	def new_screen_check(self):
		scr = self.screen()
		new = 1
		for i in self.screenhistory:
			if numpy.average(numpy.subtract(i, scr)) < 3:
				new = 0
		if new == 1:
			self.screenhistory.append(numpy.copy(scr))
	
	def scorechange(self):
		i = self.oldscore
		newscore = len(self.screenhistory)
		self.oldscore = newscore
		return newscore - i
	
	def gatherstate(self):
		return self.screen()
	
	def statesandscores(self):
		delta = self.scorechange()
		self.accumulatingrewards = [i + delta for i in self.accumulatingrewards]
		self.accumulatingrewards.append(0)
		if len(self.accumulatingrewards) > self.accumulate:
			self.finalisedrewards.append(self.accumulatingrewards.pop(0))
			self.finalisedstates.append(self.statestore.pop(0))
	
	def tick(self, num = 1):
		self.generate_inputs()
		self.pyboy.button(self.highestinput, 3)
		self.pyboy.tick(num)
		self.memory_sweep()

	def stop(self):
		self.pyboy.stop()

	def exportstates(self):
		return self.finalisedstates

	def exportrewards(self):
		return self.finalisedrewards
