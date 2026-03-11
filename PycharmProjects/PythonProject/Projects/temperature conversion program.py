
unit = input("Is this temperature in Celsius or Fahrenheit? (C or F): ")
temp = float(input("What is the temperature:"))
correct = False

if unit == "C":
    temp = temp * 9 / 5 + 32
    correct = True
elif unit == "F":
    temp = (temp - 32) * 5 / 9
    correct = True
else:
    print("Please enter either C or F")

if correct:
    print(f"Your temperature is {round(temp, 2)} {unit}")
else:
    pass
12