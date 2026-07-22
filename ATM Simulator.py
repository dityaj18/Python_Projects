#CashCounter
def greeting():
    name = input("Enter your name: ")
    print(f"\tHello {name}! Welcome to the Cash Counter.\n")
    return name

def cashNum():
    oneDoll = int(input("Enter how many $1 bills you have: "))
    fiveDoll = int(input("Enter how many $5 bills you have: "))
    tenDoll = int(input("Enter how many $10 bills you have: "))
    twenDoll = int(input("Enter how many $20 bills you have: "))
    fifDoll = int(input("Enter how many $50 bills you have: "))
    hundo = int(input("Enter how many $100 bills you have: "))
    def summary():
        print(f"\nYou have {oneDoll} $1 bills, {fiveDoll} $5 bills, {tenDoll} $10 bills, {twenDoll} $20 bills, {fifDoll} $50 bills, and {hundo} $100 bills.")
    def total():
        total = oneDoll + fiveDoll * 5 + tenDoll * 10 + twenDoll *20 + fifDoll*50 + hundo*100
        print(f"\n\tYour total amount: ${total}")
    summary()
    total()

greeting()
cashNum()