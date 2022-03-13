def SortAllWord(s):
    li = []
    words = s.split()
    words.sort()
    print("Sorted string words are: ")
    for word in words:
        l = word
        li.append(l)
        print(li)
s = input("Enter input string: ")
SortAllWord(s)
