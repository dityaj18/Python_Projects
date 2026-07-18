#Calculator to convert between different temperature scales

temp1 = input("What temperature scale to convert from? (K, C, F): ")
temp2 = input("What temperature scale to convert to? (K, C, F): ")
num = int(input("How many degrees is the temp: "))


if (temp1 == "F" and temp2 == "C"):
    F2C = int((num - 32) * (5/9))
    print(f"\n{num} degrees Fahrenheit to Celcius is {F2C}.")
elif (temp1 == "C" and temp2 == "F"):
    C2F = int((num * (9/5)) + 32)
    print(f"\n{num} degrees Celcius to Fahrenheit is {C2F}.")
elif (temp1 == "C" and temp2 == "K"):
    C2K = int(num + 273.15)
    print(f"\n{num} degrees Celcius to Kelvin is {C2K}.")
elif (temp1 == "K" and temp2 == "C"):    
    K2C = int(num - 273.15)
    print(f"\n{num} degrees Kelvin to Celcius is {K2C}.")
elif (temp1 == "F" and temp2 == "K"):
    F2K = int((num - 32) * (5/9) + 273.15)
    print(f"\n{num} degrees Fahrenheit to Kelvin is {F2K}.")
elif (temp1 == "K" and temp2 == "F"):
    K2F = int((num - 273.15) * (9/5) + 32)
    print(f"\n{num} degrees Kelvin to Fahrenheit is {K2F}.")