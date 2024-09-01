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

def printscreen():
	global screenprinted
	screenstring = ''
	for i in range(pyboy.screen.ndarray.shape[0]):
		for j in range(pyboy.screen.ndarray.shape[1]):
			screenstring += '\033[48;2;' + str(pyboy.screen.ndarray[i,j,0]) + ';' +  str(pyboy.screen.ndarray[i,j,1]) + ';' +  str(pyboy.screen.ndarray[i,j,2]) + 'm '
		screenstring += '\033[0m\n'

	screenstring += 'Game: ' + pyboy.cartridge_title + '\n'
	screenstring += 'Name: ' + name + '\n'
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
	name = ''.join(str(x) for x in pyboy.memory[0xA598:0xA5A2])


def generate_inputs():
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


for _ in range(10):
	generate_inputs()
	if inputs["up"] > 0.7:
		pyboy.button('up')
	if inputs["down"] > 0.7:
		pyboy.button("down")
	if inputs["left"] > 0.7:
		pyboy.button("left")
	if inputs["right"] > 0.7:
		pyboy.button("right")
	if inputs["a"] > 0.7:
		pyboy.button('a')
	if inputs["b"] > 0.7:
		pyboy.button('b')
	if inputs["start"] > 0.7:
		pyboy.button('start')
	if inputs["select"] > 0.7:
		pyboy.button("select")
	pyboy.tick(60)
	memory_sweep()
	printscreen()
pyboy.stop()
