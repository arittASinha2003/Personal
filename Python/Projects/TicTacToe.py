from random import *
from time import *
rounds = 0
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def game_board():
    print(" GAME BOARD ")
    print()
    print(" -  |  -  | -  " + "           1 |  2  |  3")
    print("---------------" + "           ------------")
    print(" -  |  -  | -  " + "           4 |  5  |  6")
    print("---------------" + "           ------------")
    print(" -  |  -  | -  " + "           7 |  8  |  9")
    print()


def display_board():
    print("\n")
    print(board[0] + "  |  " + board[1] + "  |  " + board[2] + "           1 |  2  |  3")
    print("--------------" + "         --------------")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5] + "           4 |  5  |  6")
    print("--------------" + "         --------------")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8] + "           7 |  8  |  9")
    print("\n")

def player_var():
    global p1
    global p2
    p1 = input("Hey! player 1 you want to be X or O - ").upper()
    while p1 not in ["X", "O"]:
        print()
        p1 = input("Hey! player 1 you want to be X or O - ").upper()
        print()
    p2 = ""
    if p1 == "X":

        p2 = "O"
        print()
        print("Player 1 X will go first")
        print()
    elif p1 == "O":

        p2  = "X"
        print()
        print("Player 2  computer X will go first")

def player_turn():
    global rounds

    while (p1 == "X" and p2 == "O") :

        rounds = rounds + 1
        pix = int(input("Hey player x where you wanna enter - ")) - 1
        while pix not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or board[pix] == "X" or board[pix] == "O":
            print()
            print()
            pix = int(input("Hey player x where you wanna enter - ")) - 1
            print()
        if board[pix] == "-":
            board[pix] = "X"
            display_board()
        else:
            print()
            print("something is wrong")
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X has won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[1] == "O" and board[2] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "O" and board[4] == "O" and board[5] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "O" and board[7] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[3] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "O" and board[4] == "O" and board[7] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[5] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[4] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[4] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[4] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif rounds == 5 and (board[0] == "X" or "O" and board[1] == "X" or "O" and board[2] == "X" or "O" and board[
            3] == "X" or "O" and board[4] == "X" or "O" and board[5] == "X" or "O" and board[6] == "X" or "O" and board[
                                  7] == "X" or "O" and board[8] == "X" or "O"):
            print()
            print("THIS IS TIE")
            print()
            break
        r1 = randint(0,2)
        r2 = randint(3,5)
        r3 = randint(6,8)
        r4 = randint(0,1)
        r5 = randint(2,3)
        r6 = randint(4,5)
        r7 = randint(6,7)
        r8 = randint(0,8)
        print()
        print("Computer is thinking")
        print()
        sleep(1)

        if board[r1] == "-" and (rounds == 1 or 2):
            board[r1] = "O"
            display_board()
        elif board[r2] == "-" and (rounds == 1 or 2 ):
            board[r2] = "O"
            display_board()
        elif board[r3] == "-" and (rounds == 3 or 4):
            board[r3] = "O"
            display_board()
        elif board[r4] == "-" and (rounds == 3 or 4):
            board[r4] = "O"
            display_board()
        elif board[r5] == "-" and (rounds == 5 or 1 or 2):
            board[r5] = "O"
            display_board()
        elif board[r6] == "-" and (rounds == 5 or 3 or 4):
            board[r6] = "O"
            display_board()
        elif board[r7] == "-" and (rounds == 1 or 3):
            board[r7] = "O"
            display_board()
        elif board[r8] == "-" and (rounds == 2 or 4):
            board[r8] = "O"
            display_board()
        else:
            print()
            print("something is wrong")
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X has won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[1] == "O" and board[2] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "O" and board[4] == "O" and board[5] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "O" and board[7] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[3] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "O" and board[4] == "O" and board[7] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[5] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[4] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[4] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[4] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif rounds == 5 and (board[0] == "X" or "O" and board[1] == "X" or "O" and board[2] == "X" or "O" and board[
            3] == "X" or "O" and board[4] == "X" or "O" and board[5] == "X" or "O" and board[6] == "X" or "O" and board[
                                  7] == "X" or "O" and board[8] == "X" or "O"):
            print()
            print("THIS IS TIE")
            print()
            break
    while (p1 == "O" and p2 == "X"):

        rounds = rounds + 1
        r1 = randint(0, 2)
        r2 = randint(3, 5)
        r3 = randint(6, 8)
        r4 = randint(0, 1)
        r5 = randint(2, 3)
        r6 = randint(4, 5)
        r7 = randint(6, 7)
        r8 = randint(0, 8)
        print()
        print("Computer is thinking")
        print()
        sleep(1)

        if board[r1] == "-" and (rounds == 1 or 2):
            board[r1] = "X"
            display_board()
        elif board[r2] == "-" and (rounds == 1 or 2):
            board[r2] = "X"
            display_board()
        elif board[r3] == "-" and (rounds == 3 or 4):
            board[r3] = "X"
            display_board()
        elif board[r4] == "-" and (rounds == 3 or 4):
            board[r4] = "X"
            display_board()
        elif board[r5] == "-" and (rounds == 5 or 1 or 2):
            board[r5] = "X"
            display_board()
        elif board[r6] == "-" and (rounds == 5 or 3 or 4):
            board[r6] = "X"
            display_board()
        elif board[r7] == "-" and (rounds == 1 or 3):
            board[r7] = "X"
            display_board()
        elif board[r8] == "-" and (rounds == 2 or 4):
            board[r8] = "X"
            display_board()
        else:
            print()
            print("something is wrong")
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X has won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[1] == "O" and board[2] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "O" and board[4] == "O" and board[5] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "O" and board[7] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[3] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "O" and board[4] == "O" and board[7] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[5] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[4] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[4] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[4] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif rounds == 5 and (board[0] == "X" or "O" and board[1] == "X" or "O" and board[2] == "X" or "O" and board[
            3] == "X" or "O" and board[4] == "X" or "O" and board[5] == "X" or "O" and board[6] == "X" or "O" and board[
                                  7] == "X" or "O" and board[8] == "X" or "O"):
            print()
            print("THIS IS TIE")
            print()
            break
        pix = int(input("Hey player O where you wanna enter - ")) - 1
        while pix not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or board[pix] == "X" or board[pix] == "O":
            print()
            print()
            pix = int(input("Hey player x where you wanna enter - ")) - 1
            print()
        if board[pix] == "-":
            board[pix] = "O"
            display_board()
        else:
            print()
            print("something is wrong")
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X has won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[1] == "O" and board[2] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[3] == "O" and board[4] == "O" and board[5] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[6] == "O" and board[7] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[3] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "X" and board[4] == "X" and board[7] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[5] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[3] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[1] == "O" and board[4] == "O" and board[7] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[5] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "X" and board[4] == "X" and board[6] == "X":
            print()
            if p1 == "X":
                print("Player 1 X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 X ")
                break
            elif p2 == "X":
                print("Player 2 Computer X you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[2] == "O" and board[4] == "O" and board[6] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif board[0] == "O" and board[4] == "O" and board[8] == "O":
            print()
            if p1 == "O":
                print("Player 1 O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 1 O ")
                break
            elif p2 == "O":
                print("Player 2 Computer O you have won the game ")
                print()
                print("CONGRATULATIONS!!! PLAYER 2 O ")
                break
        elif rounds == 5 and (board[0] == "X" or "O" and board[1] == "X" or "O" and board[2] == "X" or "O" and board[
            3] == "X" or "O" and board[4] == "X" or "O" and board[5] == "X" or "O" and board[6] == "X" or "O" and board[
                                  7] == "X" or "O" and board[8] == "X" or "O"):
            print()
            print("THIS IS TIE")
            print()
            break


def game_play():
    game_board()
    player_var()
    player_turn()


game_play()
def replay():
    print()
    r = input("Do you want to play again (y/n) -  ").upper()
    print()
    while r not in ["Y", "N"]:
        print()
        r = input("Do you want to play again (y/n) -  ").upper()
        print()
    if r == "Y":
        global rounds
        global board
        rounds = 0
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        print()
        game_play()
        print()
        replay()
    elif r == "N":
        print()
        print("THANK YOU FOR PLAYING TIC TAC TOE!!!")
        print()


replay()
