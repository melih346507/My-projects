from operator import index

foods = []
prices = []
total = 0


while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter a price of a {food}: "))
        foods.append(food)
        prices.append(price)

print("------YOUR CART------")

for food in foods:
    for price in prices:
         if foods.index(food) == prices.index(price):
             print(f"{food} --> {price}$")

for price in prices:
    total = total + price

print(f"Total price: {round(total, 2)}$")