print("--------------Welcome to Aviation Quiz Test--------------\n")
print("*Note: +2 for correct answer and -1 for incorrect answer*\n")

play = input("Do you want to play? (Yes/No): ")
if play.lower() != "yes":
    quit()

print("Okay! Let's play :)\n")

score = 0
question = 0
correct = 0

answer = input("What does ATC stand for? ")
question += 1
if answer.lower() == "air traffic control":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does VFR stand for? ")
question += 1
if answer.lower() == "visual flight rules":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does IFR stand for? ")
question += 1
if answer.lower() == "instrument flight rules":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does VMC stand for? ")
question += 1
if answer.lower() == "visual meteorological conditions":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does IMC stand for? ")
question += 1
if answer.lower() == "instrument meteorological conditions":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does VASI stand for? ")
question += 1
if answer.lower() == "visual approach slope indicator":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does PAPI stand for? ")
question += 1
if answer.lower() == "precision approach path indicator":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does ILS stand for? ")
question += 1
if answer.lower() == "instrument landing system":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does VOR stand for? ")
question += 1
if answer.lower() == "very high frequency omni-directional range":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 1

answer = input("What does NDB stand for? ")
question += 1
if answer.lower() == "non-directional beacon":
    print("Correct!")
    score += 2
    correct += 1
else:
    print("Incorrect!")
    score -= 1

print("\nYou got " + str(score) + " points!")
print("You got " + str(correct) + " out of " + str(question) + " questions correct!")

print("\nThank you for playing!\n")
