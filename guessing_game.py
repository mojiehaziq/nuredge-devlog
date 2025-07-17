# Mini Project 5: Number Guessing Game

import random

number_to_guess = random.randint(1, 10)
guess = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

while guess != number_to_guess:
    guess = int(input("Take a guess: "))
    
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it right: {number_to_guess} 🎉")
