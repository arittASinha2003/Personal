#importing necessary module
import time

#defining the functions for the letters/alphabets to be drawn in hashtag form.
def a():
    print("      #\n     # #\n    #   #\n   #     #\n  #########\n #         #\n#           #\n")

def b():
    print("########\n##      #\n##      #\n##      #\n########\n##      #\n##      #\n##      #\n########\n")

def c():
    print(" ######\n##     #\n##\n##\n##\n##\n##     #\n ######\n")

def d():
    print("######\n##    #\n##     #\n##      #\n##      #\n##      #\n##      #\n##     #\n##    #\n######\n")
    
def e():
    print("########\n##\n##\n##\n#######\n##\n##\n##\n########\n")

def f():
    print("########\n##\n##\n##\n######\n##\n##\n##\n##\n")

def g():
    print(" #########\n##       #\n##\n##\n##\n##\n##    ####\n##      ##\n #########\n")

def h():
    print("##       ##\n##       ##\n##       ##\n##       ##\n##       ##\n###########\n##       ##\n##       ##\n##       ##\n##       ##\n")

def i():
    print("##########\n    ##\n    ##\n    ##\n    ##\n    ##\n    ##\n    ##\n##########\n")

def j():
    print(" ##########\n       ##\n       ##\n       ##\n       ##\n       ##\n       ##\n  ###  ##\n ##    ##\n ##    ##\n  ######\n")

def k():
    print("##    ##\n##   ##\n##  ##\n## ##\n####\n###\n####\n## ##\n##  ##\n##   ##\n##    ##\n")

def l():
    print("##\n##\n##\n##\n##\n##\n##\n##\n##\n##\n##\n###########\n")

def m():
    print("###          ###\n## #        # ##\n##  #      #  ##\n##   #    #   ##\n##    #  #    ##\n##     ##     ##\n##            ##\n##            ##\n##            ##\n##            ##\n")

def n():
    print("###         ##\n## #        ##\n##  #       ##\n##   #      ##\n##    #     ##\n##     #    ##\n##      #   ##\n##       #  ##\n##        # ##\n##         ###\n")

def o():
    print("  ##########\n##          ##\n##          ##\n##          ##\n##          ##\n##          ##\n##          ##\n##          ##\n  ##########\n")

def p():
    print("#########\n##       #\n##        #\n##        #\n##        #\n##       #\n#########\n##\n##\n##\n##\n##\n")

def q():
    print("  ##########\n##          ##\n##          ##\n##          ##\n##          ##\n##          ##\n##       ## ##\n##        ## #\n  ######## ##\n            ##")

def r():
    print("#########\n##       #\n##        #\n##        #\n##        #\n##       #\n#########\n####\n## ##\n##  ##\n##   ##\n##    ##\n##     ##\n")

def s():
    print("  ########\n #        #\n##\n##\n #\n  ########\n          #\n          ##\n          ##\n #        #\n  ########\n")

def t():
    print("##############\n      ##\n      ##\n      ##\n      ##\n      ##\n      ##\n      ##\n      ##\n")

def u():
    print("##          ##\n##          ##\n##          ##\n##          ##\n##          ##\n##          ##\n##          ##\n##          ##\n ##        ##\n  ##########\n")

def v():
    print("##              ##\n ##            ##\n  ##          ##\n   ##        ##\n    ##      ##\n     ##    ##\n      ##  ##\n       ####\n        ##\n")

def w():
    print("##            ##\n##            ##\n##     ##     ##\n##    ####    ##\n##   ##  ##   ##\n ## ##    ## ##\n  ###      ###\n")

def x():
    print("##        ##\n ##      ##\n  ##    ##\n   ##  ##\n    ####\n     ##\n    ####\n   ##  ##\n  ##    ##\n ##      ##\n##        ##\n")

def y():
    print("##        ##\n ##      ##\n  ##    ##\n   ##  ##\n    ####\n     ##\n     ##\n     ##\n     ##\n     ##\n")

def z():
    print("#############\n##        ##\n         ##\n        ##\n       ##\n      ##\n     ##\n    ##\n   ##\n  ##\n ##        ##\n#############\n")

def dot():
    print(" .....\n.......\n.......\n .....\n")

def space():
    print("\n"*4)
    
#If user input includes any of the signs of "invalid_signs" variable, then it will turn on the "invaid_signs_switch"
invalid_signs = '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', ';', ',', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?'

#invalid signs switch is off now
invalid_signs_switch = False

#The 'no_error' switch is set 'on' so that the program goes normally when everything is normal.
no_error = True

#Taking string input from the user
user_name = input("Enter your name: ")

#The value of any variable 'Q' is set for limiting the loop according to the string length.

#The value of Q also plays an important role in maintaining the string's serial of the alphabets.
Q = 0

#The range of the 'for' loop is set equal to the length of the string so that the loop breaks after reading the last alphabet of the string.
for X in range(len(user_name)):

#This 'for' loop is confirming the position of each letter
    if user_name[Q].lower() == "a":
        print("A is written at ")
        pass

#I am using ".lower()" string method so that no error happens when user inputs capital letters. 
    elif user_name[Q].lower() == "b":
        print("B is written at ")
        pass

    elif user_name[Q].lower() == "c":
        print("C is written at ")
        pass

    elif user_name[Q].lower() == "d":
        print("D is written at ")
        pass

    elif user_name[Q].lower() == "e":
        print("E is written at ")
        pass

    elif user_name[Q].lower() == "f":
        print("F is written at ")
        pass

    elif user_name[Q].lower() == "g":
        print("G is written at ")
        pass

    elif user_name[Q].lower() == "h":
        print("H is written at ")
        pass

    elif user_name[Q].lower() == "i":
        print("I is written at ")
        pass

    elif user_name[Q].lower() == "j":
        print("J is written at ")
        pass

    elif user_name[Q].lower() == "k":
        print("K is written at ")
        pass

    elif user_name[Q].lower() == "l":
        print("L is written at ")
        pass

    elif user_name[Q].lower() == "m":
        print("M is written at ")
        pass

    elif user_name[Q].lower() == "n":
        print("N is written at ")
        pass

    elif user_name[Q].lower() == "o":
        print("O is written at ")
        pass

    elif user_name[Q].lower() == "p":
        print("P is written at ")
        pass

    elif user_name[Q].lower() == "q":
        print("Q is written at ")
        pass

    elif user_name[Q].lower() == "r":
        print("R is written at ")
        pass

    elif user_name[Q].lower() == "s":
        print("S is written at ")
        pass

    elif user_name[Q].lower() == "t":
        print("T is written at ")
        pass

    elif user_name[Q].lower() == "u":
        print("U is written at ")
        pass

    elif user_name[Q].lower() == "v":
        print("V is written at ")
        pass

    elif user_name[Q].lower() == "w":
        print("W is written at ")
        pass

    elif user_name[Q].lower() == "x":
        print("X is written at ")
        pass

    elif user_name[Q].lower() == "y":
        print("Y is written at ")
        pass

    elif user_name[Q].lower() == "z":
        print("Z is written at ")
        pass

    elif user_name[Q] == ".":
        print("a dot is in ")
        pass

    elif user_name[Q] == " ":
        print("a space is in ")
        pass

#If user input contains special characters, an "skip" message is shown along with its position
    elif user_name[Q] in invalid_signs:
        print("an invalid sign is skipped at")
        pass
        
#if something goes wrong, the else statement will be executed and the no_error switch is turned off so that the finishing doen't go normally
    else:
        print("Something went wrong")
        no_error = False
        break

#these 'while' loops print out the positions serially
    while Q<=2:
        if Q == 0:
            print("1st position\n")
            time.sleep(1)
            break
        elif Q == 1:
            print("2nd position\n")
            time.sleep(1)
            break
        elif Q == 2:
            print("3rd postion\n")
            time.sleep(1)
            break
    Y = str(Q+1)

    while Q>=3:
        print(Y + "th position\n")
        time.sleep(1)
        break

#The value of Q changes after each complete loop
    Q+=1

#Starting another loop by resetting the value of 'Q'
Q = 0

for Y in range(len(user_name)):

#This 'for' loop is made for printing the letters in hashtag(#) form by calling those functions
    if user_name[Q].lower() == "a":
        a()
        pass

    elif user_name[Q].lower() == "b":
        b()
        pass

    elif user_name[Q].lower() == "c":
        c()
        pass

    elif user_name[Q].lower() == "d":
        d()
        pass

    elif user_name[Q].lower() == "e":
        e()
        pass

    elif user_name[Q].lower() == "f":
        f()
        pass

    elif user_name[Q].lower() == "g":
        g()
        pass

    elif user_name[Q].lower() == "h":
        h()
        pass

    elif user_name[Q].lower() == "i":
        i()
        pass

    elif user_name[Q].lower() == "j":
        j()
        pass

    elif user_name[Q].lower() == "k":
        k()
        pass

    elif user_name[Q].lower() == "l":
        l()
        pass

    elif user_name[Q].lower() == "m":
        m()
        pass

    elif user_name[Q].lower() == "n":
        n()
        pass

    elif user_name[Q].lower() == "o":
        o()
        pass

    elif user_name[Q].lower() == "p":
        p()
        pass

    elif user_name[Q].lower() == "q":
        q()
        pass

    elif user_name[Q].lower() == "r":
        r()
        pass

    elif user_name[Q].lower() == "s":
        s()
        pass

    elif user_name[Q].lower() == "t":
        t()
        pass

    elif user_name[Q].lower() == "u":
        u()
        pass

    elif user_name[Q].lower() == "v":
        v()
        pass

    elif user_name[Q].lower() == "w":
        w()
        pass

    elif user_name[Q].lower() == "x":
        x()
        pass

    elif user_name[Q].lower() == "y":
        y()
        pass

    elif user_name[Q].lower() == "z":
        z()
        pass

    elif user_name[Q] == ".":
        dot()
        pass
    
    elif user_name[Q] == " ":
        space()
        pass

#The invalid_signs switch is turned on if user input contains any special characters and nothing gets printed out.

#But it will print an apology message at the end
    elif user_name[Q] in invalid_signs:
        invalid_signs_switch = True
        pass

#When all of the "if" statements fails, the else statement prints out an error message. And breaks the loop.

#The no_error switch is turned off so that the finishing doesn't go normally
    else:
        print("Maybe some inputs are invalid.")
        no_error = False
        break
        
#the value of Q changes after each complete loop
    Q+=1

#when everything finishes normally without any error, the no_error switch stays 'on' and the finishing goes normal too.
if no_error == True:    

    #when the "invalid signs" switch is on, it prints a sorry message
    if invalid_signs_switch == True:
        print("Sorry " + user_name + " I had to skip numbers and special characters.\nBut,")
        pass

    #when the invalid_input switch is off it doesn't print any sorry message 
    elif invalid_signs_switch == False:
        print("Now,")
        pass

#when the if statements fail to work, the else statement shows an error message and closes the program
    else:
        print("An unknowon error occurred")
        exit()
    print("Watch the magic.\n Scroll up and see. ")

#Asking feedback from the user
    print("Thank you " + user_name + " for trying my program.")

#When the no_error switch gets 'off' for any kind of error, the program apologizes and gives a suggestion to avoid such errors.
elif no_error == False:
    print("I am really sorry for this error.\nPlease try again and try not to use special signs.")

#when everything fails, the program gets closed directly
else:
    print("Error")
    exit()
