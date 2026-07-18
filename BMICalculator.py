#Calculates BMI based on weight and height

y = True
while y == True:
    weight = input("What is your body weight in pounds(lbs): ")
    height = input("What is your height in inches(in): ")
    try:
        weight = float(weight)
        height = float(height)
        y = False
    except:
        print("Error, invalid input for weight or height! Please try again.\n")

bmi = (weight / height**2) * 703

print(f"\nYour Body Mass Index (BMI) is {bmi:.2f}")
