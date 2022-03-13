def pypart2(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ") # gap matters
        k = k - 2
        for j in range(0,i+1):
            print("* ", end = "") # gap matters
        print("\r")
n = 3
pypart2(n)
