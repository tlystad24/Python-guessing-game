#!/usr/bin/env python
"""Python guessing game by @tlystad24
This program creates a random number between 1 and 100 and has the user guess it.
"""
import random

def main():
	print "Guess a number netween 1 and 100."
	#randomNumber = 35 <- Number used for debugging and early development.
	randomNumber = random.randint(1,100)
	found = False # flag variable to see if they guessed it.

	while not found:
	
		userGuess = input("Your guess: ")
		if userGuess == randomNumber:
			print ("You have guessed the correct number!")
			found = True
			
		elif userGuess > randomNumber:
			print ("Guess lower!")
		
		else:
			print ("Guess higher!")

				



if __name__ == "__main__":
	main()
