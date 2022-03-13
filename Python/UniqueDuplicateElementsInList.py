def duplicate(l):
    uni = []
    dup = []
    for i in range(0,len(l)):
        k = i + 1
        for j in range(k,len(l)):
            if l[i] == l[j] and l[i] not in dup:
                dup.append(l[i])
        if l[i] not in dup:
            uni.append(l[i])
    print("Unique elements are: ",uni)
    print("Duplicate elements are: ",dup)

x = []
n = int(input("Enter number of elements in list: "))
for i in range(0,n):
    m = int(input("Enter an element: "))
    x.append(m)
print("Given list: ",x)
duplicate(x)
