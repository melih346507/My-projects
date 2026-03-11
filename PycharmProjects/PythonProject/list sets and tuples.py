# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but A dd/Remove OK. NO duplicates
# tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "banana", "cherry", "coconut"]

#print(fruits[::2])
print(help(fruits))
#print(len(fruits))
#print("apple" in fruits)
#print("elma" in fruits)

#fruits[0] = "elma"
#fruits.append("mango")
#fruits.remove("apple")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()


for fruit in fruits:
    print(fruit, end=" ")

