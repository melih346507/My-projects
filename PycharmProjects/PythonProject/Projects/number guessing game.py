import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guess_num = 0

print("---------GUESS-THE-NUMBER---------")
print()

while True:
    guess = input(f"Guess a number between {lowest_num} and {highest_num} (q to quit): ").lower()

    if guess.isdigit():
        guess = int(guess)
        if highest_num >= guess >= lowest_num:
            if guess == answer:
                print("Correct!")
                guess_num += 1
                break
            elif guess < answer:
                print("Too low!")
                guess_num += 1
            elif guess > answer:
                print("Too high!")
                guess_num += 1
        else:
            print(f"Please enter a number between {lowest_num} and {highest_num}!")
    elif guess == "q":
        break
    else:
        print("Please enter a number!")


print("--------------SCORE--------------")
print(f"The correct number was {answer}")
print(f"You guessed {guess_num} times!")
if guess == "q":
    print("You couldn't find the number!")
else:
    print("You guessed the number!")
print("---------------------------------")

