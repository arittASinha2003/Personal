Boy = input("Enter boy's name: ")
Girl = input("Enter girl's name: ")
print("Select side: ")
print("1. Boy loves Girl")
print("2. Girl loves Boy")
print("3. Both Boy and Girl loves each other")
choice = input("Enter choice (1/2/3): ")
if choice == '1':
    print(Boy,"loves",Girl)
elif choice == '2':
    print(Girl,"loves",Boy)
elif choice == '3':
    print("Both",Boy,"and",Girl,"loves each other")
else:
    print("Invalid input")
