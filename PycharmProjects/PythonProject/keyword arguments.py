

#def hello(greeting, title, first, last):
#    print(f"{greeting.capitalize()} {title} {first} {last}")

#hello("hello", title="Mr. ", last="Spongbob", first="Squarepants")

#for x in range(1,11):
#    print(x,end=" ")

#print("1", "2", "3", "4", "5", "6", "7", "8", "9", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=90, area=539, first=542, last=9686)
print(phone_num)