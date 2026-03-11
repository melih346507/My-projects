
username = input("Enter your username: ")

if len(username) < 12 and username.count(" ") == 0 and username.isalpha():
    print("Your username is valid")
else:
    print("Your username is invalid")
    print("Please make sure your username contains only letters and shorter than 12 carecters")