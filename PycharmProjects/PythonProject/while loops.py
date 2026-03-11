
#name = input("Enter your name: ")

#while name == "":
#    print("Yuo did not enter your name")
#    name = input("Enter your name: ")
#else:
#    print(f"Hello {name}")

###############################3

#age = int(input("Enter your age: "))

#while age < 0:
#    print("Your age must be greater than or equal to zero.")
#    age = int(input("Enter your age: "))

#print(f"Your age is {age} years old.")

##################################

#food = input("Enter your favorite food (q to quit): ")

#while not food == "q":
#    print(f"Your favorite food is {food}")
#    food = input("Enter your favorite food (q to quit): ")

#print("Bye")

###################################

num = int(input("Enter a number between 1 and 10: "))

while num > 10 or num < 1:
    print("Please enter a number between 1 and 10")
    num = int(input("Enter a number between 1 and 10: "))

print(f"Thank you, your number is {num}!")