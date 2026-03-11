import random
print("---------------------------")
print("Welcome to the Rock Paper Scissors game")
print("---------------------------")
running = True
while running:

    player = None
    options = ("rock", "paper", "scissors")
    x = ("r", "p", "s")
    computer = random.choice(options)



    while player not in x:
        player = input("Enter rock, paper, or scissors (r,p or s): ").lower()
        if player not in x:
            print("Please enter rock, paper, or scissors")

    if player == "r":
        player = "rock"
        print(f"You chose {player}")
        print(f"Computer chose {computer}")
    elif player == "p":
        player = "paper"
        print(f"You chose {player}")
        print(f"Computer chose {computer}")
    elif player == "s":
        player = "scissors"
        print(f"You chose {player}")
        print(f"Computer chose {computer}")


    print("---------------------------")

    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer == "scissors":
        print("You loose")
    elif player == "scissors" and computer == "rock":
        print("You loose")
    elif player == "rock" and computer == "paper":
        print("You loose")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "n":
        running = False
print()
print("---------------------------")
print("Thank you for playing... :D")
print("---------------------------")