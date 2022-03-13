string = input("Enter a string: ")
word = input("Enter a word: ")
a = []
count = 0
a = string.split(" ")
for i in range(0,len(a)):
    if(word==a[i]):
        count = count + 1
print("Count of the word is:")
print(count)
