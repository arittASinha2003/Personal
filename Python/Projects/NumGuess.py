import random

print("----------Welcome to Number Guessing Game!----------\n")

play = input("Do you want to play? (Yes/No): ")
if play.lower() != "yes":
    quit()

print("Okay! Let's play :)\n")

tries = 0

top = int(input("Enter the top number (range): "))
number = random.randint(0, top)

while True:
    guess = int(input("Guess the number: "))
    if guess == number:
        print("\nCorrect!")
        print("The number was", number)
        tries += 1
        print("You got it in", tries, "tries.")
        break
    elif guess > number:
        print("Too high!")
        tries += 1
    elif guess < number:
        print("Too low!")
        tries += 1

print("\nThanks for playing!\n")
