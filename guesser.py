#!/usr/bin/env python
# text-based guessing game written in Python by @tlystad24


# Import random library to generate the number to guess.
import random


def main():
    attempts = 1  # Initial count of attempts. Minimum is 1.
    print "How many numbers do you want?"
    # Declare variable to generate random number inside range.
    howMany = input("Ammount: ")
    if howMany == 1:
        print "Pick a number greater than 1!"
        main()  # If the number is 1, return to main.

    else:  # if the number is greater than 1, continue.
        print 'Guess the number between 1 and {}.'.format(howMany)
        randomNumber = random.randint(1, howMany)
        found = False  # declare found as false.

        while not found:  # while the user has not guessed the correct number.

            userGuess = input("Your guess: ")
            if userGuess == randomNumber:
                print "You have guessed the correct number! You used", attempts, "attempts."
                found = True  # declare found as true which ends the program

            elif userGuess > randomNumber:  # if the user is less than the generated number
                print ("Guess lower!")
                attempts = attempts + 1  # add one attempt to the counter
            else:
                print ("Guess higher!")
                attempts = attempts + 1  # add one attempt to the counter


if __name__ == "__main__":
    main()
