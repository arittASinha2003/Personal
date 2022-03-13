Person1 = input("Enter 1st person's name: ")
Person2 = input("Enter 2nd person's name: ")
print("Select type: ")
print("1. Love")
print("2. Like")
print("3. Friend")
print("4. Best Friend")
choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    print("Select side: ")
    print("1. Person1 loves Person2")
    print("2. Person2 loves Person1")
    print("3. Both Person1 and Person2 loves each other")
    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        print(Person1,"loves",Person2)
    elif choice == '2':
        print(Person2,"loves",Person1)
    elif choice == '3':
        print("Both",Person1,"and",Person2,"loves each other")
    else:
        print("Invalid input")
elif choice == '2':
    print("Select side: ")
    print("1. Person1 likes Person2")
    print("2. Person2 likes Person1")
    print("3. Both Person1 and Person2 likes each other")
    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        print(Person1,"likes",Person2)
    elif choice == '2':
        print(Person2,"likes",Person1)
    elif choice == '3':
        print("Both",Person1,"and",Person2,"likes each other")
    else:
        print("Invalid input")
elif choice == '3':
    print("Select side: ")
    print("1. Person1 is Person2's friend")
    print("2. Person2 is Person1's friend")
    print("3. Both Person1 and Person2 are friends")
    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        print(Person1,'is',Person2,"'s friend")
    elif choice == '2':
        print(Person2,'is',Person1,"'s friend")
    elif choice == '3':
        print("Both",Person1,"and",Person2,"are friends")
    else:
        print("Invalid input")
elif choice == '4':
    print("Select side: ")
    print("1. Person1 is Person2's best friend")
    print("2. Person2 is Person1's best friend")
    print("3. Both Person1 and Person2 are best friends")
    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        print(Person1,'is',Person2,"'s best friend")
    elif choice == '2':
        print(Person2,'is',Person1,"'s best friend")
    elif choice == '3':
        print("Both",Person1,"and",Person2,"are best friends")
    else:
        print("Invalid input")
else:
    print("Invalid input")
