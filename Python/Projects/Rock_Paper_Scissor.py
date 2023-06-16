import random

print("----------Welcome to Rock/Paper/Scissor Game!----------\n")

play = input("Do you want to play? (Yes/No): ")
if play.lower() != "yes":
    quit()

print("Okay! Let's play :)\n")

user_win = 0
comp_win = 0
ties = 0

options = ["rock", "paper", "scissor"]

while True:
    user = input("Rock, Paper, or Scissor? (or Stop): ").lower()
    if user == "stop":
        break
    if user not in options:
        print("Invalid Input, try again!")
        continue

    comp = random.choice(options)
    print("Computer choose", comp + ".")

    if user == comp:
        print("It's a tie!")
        ties += 1
    elif user == "rock" and comp == "scissor":
        print("You win!")
        user_win += 1
    elif user == "paper" and comp == "rock":
        print("You win!")
        user_win += 1
    elif user == "scissor" and comp == "paper":
        print("You win!")
        user_win += 1
    else:
        print("You lose!")
        comp_win += 1

print("\nYou won", user_win, "times.")
print("Computer won", comp_win, "times.")
print("We tied", ties, "times.")

print("\nThanks for playing!\n")
