
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Please enter the principle amount: "))
    if principle <= 0:
        print("Please enter a positive number")

while rate <= 0:
    rate = float(input("Please enter the rate amount: "))
    if rate <= 0:
        print("Please enter a positive number")

while time <= 0:
    time = float(input("Please enter the time amount: "))
    if time <= 0:
        print("Please enter a positive number")

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} years: ${total:.2f}")