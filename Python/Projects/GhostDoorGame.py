from random import randint
print("Ghost Game")
print("Three doors are in front of you")
print("One of them has a ghost inside of it")
print("Choose wisely")

running = True
score = 0

while running:
    ghost_door = randint(1,3)
    door = input("Here are your choices: 1, 2 or 3: ")
    door_num = int(door)
    if door_num == 1:
        if door_num == ghost_door:
            print("Ghost")
            running = False
        else:
            print("No ghost")
            print("You can advance to the next room")
            score += 1

    elif door_num == 2:
        if door_num == ghost_door:
            print("Ghost")
            running = False
        else:
            print("No ghost")
            print("You can advance to the next room")
            score += 1

    elif door_num == 3:
        if door_num == ghost_door:
            print("Ghost")
            running = False
        else:
            print("No ghost")
            print("You can advance to the next room")
            score += 1

    else:
        print("This is not a valid number")

print("Game over")
print("You ran into a ghost. Your score is",score)
