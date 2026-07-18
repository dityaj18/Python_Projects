#Calculate a student's letter grade depending on their number grade

valid = input("Would you like to use the grade calculator? (Y/N): ")

while (valid == "Y"):    
    grade = int(input("Enter the grade: "))
    
    if (grade >= 90):
        print("Student got an A.")
    elif (grade >= 80):
        print("Student got a B.")
    elif (grade >= 70):
        print("Student got a C.")
    elif (grade >= 60):
        print("Student got a D.")
    elif (grade <= 59):
        print("Student got a F.")
    
    valid = input("Would you like to use it again? (Y/N): ")

print("\nGoodbye.")