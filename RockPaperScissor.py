#RockPaperScissors
import random

def greet():
    name = input("Enter your name: ")
    print(f"Hello {name}! Welcome to Rock, Paper, Scissors against Robot!")
    return name
def playerChoice():
    choice = input("\tChoose rock, paper, or scissors: ").lower()
    return choice
def robotChoice():
    options = ["rock", "paper", "scissors"]
    roboChoice = random.choice(options)
    print("\nRobot chose: " + roboChoice)
    return roboChoice
def winner():
    if (choice == "scissors"):
        if (roboChoice == "rock"):
            print("Rock beats scissors! Robot wins!")
        elif (roboChoice == "paper"):
            print(f"Scissors beats paper! {name} wins!")
        else:
            print("It's a tie!")
    
    elif (choice == "rock"):
        if (roboChoice == "scissors"):
            print(f"Rock beats scissors! {name} wins!")
        elif (roboChoice == "paper"):
            print("Paper beats rock! Robot wins!")
        else:
            print("It's a tie!")
    
    elif (choice == "paper"):
        if (roboChoice == "rock"):
            print(f"Paper beats rock! {name} wins!")
        elif (roboChoice == "scissors"):
            print("Scissors beats paper! Robot wins!")
        else:
            print("It's a tie!")
            
    else:
        print("Error! Invalid input.")
    
name = greet()
choice = playerChoice()
roboChoice = robotChoice()
winner()

    
print("\n\tGame finished")