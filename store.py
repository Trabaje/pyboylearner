#storin useful code which is too much hassle to comment in and out, for copy & paste

	screenstring += 'Game: ' + pyboy.cartridge_title + '\n'
	screenstring += 'Screens: ' + str(accumulatingrewards) + '\n'
	screenstring += 'Scores/States: ' + str(len(accumulatingrewards)) + ' ' + str(len(finalisedrewards)) + ' ' + str(len(statestore)) + ' ' + str(len(finalisedstates)) + '\n'
	screenstring += 'Up: ' + str(inputs["up"]) + '\n'
	screenstring += 'Down: ' + str(inputs ["down"] ) + '\n'
	screenstring += 'Left: ' + str(inputs["left"]) + '\n'
	screenstring += 'Right: ' + str(inputs["right"]) + '\n'
	screenstring += 'A: ' + str(inputs["a"]) + '\n'
	screenstring += 'B: ' + str(inputs["b"]) + '\n'
	screenstring += 'Start: ' + str(inputs["start"]) + '\n'
	screenstring += 'Select: ' +str(inputs["select"]) + '\n'