#!/usr/bin/env python
"""Python guessing game by @tlystad24
This program creates a random number between 1 and 100 and has the user guess it.
"""
import random

def main():
	attempts = 1
	print "How many numbers do you want?"
	howMany = input("Ammount: ")
	# print "Guess the number between 1 and",howMany,"."
	print 'Guess the number between 1 and {}.'.format(howMany)
	#randomNumber = 35 <- Number used for debugging and early development.
	randomNumber = random.randint(1,howMany)
	found = False # flag variable to see if they guessed it.

	while not found:

		userGuess = input("Your guess: ")
		if userGuess == randomNumber:
			print "You have guessed the correct number! You used",attempts,"attempts."
			found = True

		elif userGuess > randomNumber:
			print ("Guess lower!")
			attempts = attempts + 1
		else:
			print ("Guess higher!")
			attempts = attempts +1





if __name__ == "__main__":
	main()
