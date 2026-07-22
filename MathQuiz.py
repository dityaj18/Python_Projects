#MathQuiz
import random

def greeting():
    name = input("Enter your name: ")
    return name
def addition():
    num1 = random.randrange(0,21)
    num2 = random.randrange(0,21)
    ans = int(input(f"What is {num1} + {num2}: "))
    if (ans == (num1 + num2)):
        print("Correct!")
    else:
        print("Wrong!")
    return ans
def subtraction():
    num1 = random.randrange(0,21)
    num2 = random.randrange(0,21)
    ans = int(input(f"What is {num1} - {num2}: "))
    if (ans == (num1 - num2)):
        print("Correct!")
    else:
        print("Wrong!")
    return ans

name = greeting()
questionNum = int(input("How many questions do you want in the quiz? "))
operators = [addition, subtraction]
operQuiz = random.choice(operators)

i = 0
while (i < questionNum):
    operQuiz()
    i += 1
    
print("\n\tEnd of quiz!")