string = input("Enter a string: ")
count = 0
for i in string:
    if(i.islower()):
        count = count + 1
print("The number of lowercase characters: ")
print(count)
