n = int(input("Enter number of terms: "))
for j in range(1,n+1):
    a = []
    for i in range(1,j+1):
        print(i,sep = " ",end = " ")
        if(i<j):
            print("+",sep = " ",end = " ")
        a.append(i)
    print("=",sum(a))
print()
