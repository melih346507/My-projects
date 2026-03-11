
rows = int(input("How many rows would you like? "))
columns = int(input("How many columns would you like? "))
symbol = input("What symbol would you like?: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()