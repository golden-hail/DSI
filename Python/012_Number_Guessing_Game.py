# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:23:15 2026

@author: aiaqu
"""

# Version 1
CORRECT_NUMBER = 26 # constants as upper case

user_guess = input("Guess a number: ")

if user_guess == CORRECT_NUMBER:
    print("Wow! You are great at guessing")
else:
    print("Sorry, you guess is incorrect")
    
# Version 2
CORRECT_NUMBER = 26 # constants as upper case

while True:
    user_guess = input("Guess a number: ")
    
    if user_guess == CORRECT_NUMBER:
        print("You win! Wow! You are great at guessing")
        break
    else:
        print("Sorry, you guess is incorrect")
        print("Please guess again")

# Version 3 # RANDOM: a python module

import random

random.randint(1,10)

LOWER_BOUND = 1
UPPER_BOUND = 100
GUESS_LIMIT = 5
GUESS_COUNTER = 0
CORRECT_NUMBER = random.randint(LOWER_BOUND,UPPER_BOUND)

print(f"Try guessing the number that I'm thinking. It is between {LOWER_BOUND} and {UPPER_BOUND}")

while True:
    user_guess = int(input("Guess a number: "))
    GUESS_COUNTER += 1
    remaining_guesses = GUESS_LIMIT - GUESS_COUNTER
    
    if LOWER_BOUND <= user_guess <= UPPER_BOUND:
        if user_guess == CORRECT_NUMBER:
            print("Wow! You got it in {GUESS_COUNTER} guesses!")
            break
        elif user_guess < CORRECT_NUMBER:
            print(f"Your guess is too low, try again! Guesses remaining: {remaining_guesses}")
        else:
            print(f"Your guess is too High, try again! Guesses remaining: {remaining_guesses}")
            
    else:
        print(f"Number {user_guess} is not within the bounds of the game. Number must be between {LOWER_BOUND} and {UPPER_BOUND}")

    if remaining_guesses == 0:
        print(f"Sorry, you are out of guesses. The correct number was {CORRECT_NUMBER}")
        break