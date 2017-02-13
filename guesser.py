#!/usr/bin/env python
"""guesser.py, by Tobias Lystad
This program creates a random number between 1 and 100 and has the user guess it.
"""
import random

def main():
	print "Guess a number netween 1 and 100."
	#randomNumber = 35
	randomNumber = random.randint(1,100)
	found = False # flag variable to see if they guessed it

	while not found:
	
		userGuess = input("Your guess: ")
		if userGuess == randomNumber:
			print ("Correct!")
			found = True
			
		elif userGuess > randomNumber:
			print ("Guess lower!")
		
		else:
			print ("Guess higher!")

				



if __name__ == "__main__":
	main()