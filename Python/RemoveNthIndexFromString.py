def remove(string,n):
    first = string[:n]
    last = string[n+1:]
    return first + last
string = input("Enter the string: ")
n = int(input("Enter the index of the character to remove (include zero): "))
print("Modified string: ")
print(remove(string,n))
