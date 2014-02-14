while True:

	print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

	door = raw_input("> ")

	if door == "1":
		print "There's a giant bear here eating a cheese cake. What do you do?"
		print "1. Take the cake."
		print "2. Scream at the bear."
	
		bear = raw_input("> ")
	
		if bear == "1":
			print "The bear eats your face off. You are dead."
			break
		elif bear == "2":
			print "The bear eats your legs off. Sorry."
			break
		else:
			print "Well, doing %s is probably better. The bear runs away." % bear
			break

	elif door == "2":
		print "You find Nate working on his Burrito Bracket data. What do you do?"
		print "1. Tell him burritos are all the same, and life is meaningless."
		print "2. Smash a burrito on his computer."
		print "3. Tell him you're excited to see which burrito wins."
	
		burrito = raw_input("> ")
	
		if burrito == "1" or burrito == "2":
			print "Nate fires you, then feeds you to a bear in the next room."
			break
		if burrito == "3":
			print "Nate thanks you and hands you a cake."
			break

	elif door == "neither":
		print "Wow! You've reached a secret level.\nWhat's your name?"
		
		name = raw_input("> ")
		
		print "Well %s, now that you are in this secret level, what do you want to do?" % name
		print "1. Go back to the doors."
		print "2. Stop playing."
		
		secret = raw_input("> ")
		
		if secret == "2":
			print "Okay, you're done."
			break
			
	else:
		print "You don't really get how to play this game. A bear eats you."
		break
		