l = [1, 9, 7, 2, 8, 5, 3]
for j in range(0,len(l)):
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
print(l)
