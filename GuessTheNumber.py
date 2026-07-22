#NumberGuess
import random

def greeting():
    name = input("Enter your name: ")
    print(f"Hello " + name + "! Welcome to Guess The Number.\n")
    return name
def playerGuess():
    guess = int(input("Guess the number from 0-20: "))
    return guess
def rightNumber():
    num1 = random.randrange(0,21)
    return num1
def guessLogic(guess, num1):
    while (guess != num1):
        if (guess > num1):
            print("\tIncorrect!!Hint: the number is lower.")
        elif (guess < num1):
            print("\tIncorrect! Hint: the number is higher.")
        guess = int(input("\nGuess again: "))
        if (guess == num1):
            print(f"\nCorrect! The number was {num1}")

name = greeting()
guess = playerGuess()
num1 = rightNumber()
guessLogic(guess, num1)
    
print("Goodbye.")