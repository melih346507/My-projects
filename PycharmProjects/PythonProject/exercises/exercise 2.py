# Shopping cart program

item = input("Ne almak istersin?: ")
price = float(input("Kaç para baba?: "))
quantity = float(input("Kaç tane alacan?: "))
total = price * quantity

print(f"Kral {quantity} tane {item} aldın")
print(f"{total} para ödicen")