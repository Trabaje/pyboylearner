from pyboy import PyBoy

import sys
import numpy
import random

numpy.set_printoptions(threshold=sys.maxsize)

pyboy = PyBoy('files/rom.gb')
pyboy.set_emulation_speed(0)

screenprinted = 0

name = [' ']
inputs = {
"up": 0.0,
"down": 0.0,
"left": 0.0, 
"right": 0.0,
"b": 0.0,
"a": 0.0,
"select": 0.0,
"start": 0.0
}
highestinput = ""

screenhistory = []

def printscreen():
	global screenprinted, name, screenhistory
	screenstring = ''
	for i in range(pyboy.screen.ndarray.shape[0]):
		for j in range(pyboy.screen.ndarray.shape[1]):
			screenstring += '\033[48;2;' + str(pyboy.screen.ndarray[i,j,0]) + ';' +  str(pyboy.screen.ndarray[i,j,1]) + ';' +  str(pyboy.screen.ndarray[i,j,2]) + 'm '
			x = 1
		screenstring += '\033[0m\n'

	screenstring += 'Game: ' + pyboy.cartridge_title + '\n'
	screenstring += 'Screens: ' + str(len(screenhistory)) + '\n'
	screenstring += 'Up: ' + str(inputs["up"]) + '\n'
	screenstring += 'Down: ' + str(inputs ["down"] ) + '\n'
	screenstring += 'Left: ' + str(inputs["left"]) + '\n'
	screenstring += 'Right: ' + str(inputs["right"]) + '\n'
	screenstring += 'A: ' + str(inputs["a"]) + '\n'
	screenstring += 'B: ' + str(inputs["b"]) + '\n'
	screenstring += 'Start: ' + str(inputs["start"]) + '\n'
	screenstring += 'Select: ' +str(inputs["select"]) + '\n'
	
	refresh = ''
	if screenprinted == 1:
		for _ in range(screenstring.count('\n')+1):
			refresh += '\033[A'

	print(refresh + screenstring)
	sys.stdout.flush()
	screenprinted = 1

def memory_sweep():
	global name
	name = ''.join(str(x) for x in pyboy.memory[0xD47D:0xD486])
	new_screen()


def generate_inputs():
	global highestinput
	inputs.update( {
		"up": random.uniform(0,1),
		"down": random.uniform(0,1),
		"left" : random.uniform(0,1),
		"right": random.uniform(0,1),
		"b": random.uniform(0,1),
		"a" : random.uniform(0,1),
		"select": random.uniform(0,1),
		"start": random.uniform(0,1)
	} )
	highestinput = max(inputs, key = inputs.get)

def new_screen():
	global screenhistory, pyboy
	screen = pyboy.screen.ndarray #[66:80, 64:72, 0]
	new = 1
	for i in screenhistory:
		#if numpy.array_equal(screen, i):
		if numpy.average(numpy.subtract(i, screen)) < 5:
			#print(numpy.average(numpy.subtract(i, screen)))
			new = 0
	if new == 1:
		screenhistory.append(numpy.copy(screen))


for _ in range(500):
	generate_inputs()
	pyboy.button(highestinput, 3)
	pyboy.tick(50)
	memory_sweep()
	printscreen()
pyboy.stop()
