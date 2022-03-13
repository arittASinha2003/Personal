def pattern(n):
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("1 ",end = "")
        print("\r")
pattern(2)
