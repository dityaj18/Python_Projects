#Calculates tip based on percentage

print("-----Welcome to the tip calculator!-----")
valid = input("Would you like to use the calculator? (Y/N) ")

while (valid == "Y"):
    price = float(input("Enter the sub-total (do NOT include the $ symbol): "))
    percent = float(input("Enter the tip percentage(do NOT include the % symbol): "))
    
    tip = percent / 100 + 1
    
    total = (price * tip)
    
    print(f"The total is {total}")
    valid = input("Would you like to use the calculator again?(Y/N) ")
    
print ("---Thank you---")