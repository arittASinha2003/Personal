string = input("Enter a string: ")
sub_str = input("Enter a word: ")
if(string.find(sub_str)==-1):
    print("Substring not found in string!")
else:
    print("Substring found in string!")
