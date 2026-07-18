name = input("Enter your name: ")

valid = input("Would you like to use the calculator? (Y/N): ")
while (valid == "Y"):
    func = input("Choose a math function (+, -, *, /): ")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    print(f"The 2 numbers you chose are {num1} and {num2}, and the math function you chose is {func}.")
    
    if (func == "+"):
        print(f"Calculating answer... \n")
        ans = num1 + num2
        print(f"{num1} + {num2} is {ans}")
    elif (func == "-"):
        print(f"Calculating answer... \n")
        ans = num1 - num2
        print(f"{num1} - {num2} is {ans}")
    elif (func == "*"):
        print(f"Calculating answer of... \n")
        ans = num1 * num2
        print(f"{num1} * {num2} is {ans}")
    elif (func == "/"):
        print(f"Calculating answer of... \n")
        ans = num1 / num2
        print(f"{num1} / {num2} is {ans}")
    valid = input("Would you like to keep using? (Y/N): ")
    
print("\nSee you next time!")