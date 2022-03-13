l = [2,1,0,4,3]
for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)


l = [4,2,1,0,7]
for i in range(0,len(l)):
    pos = i
    for j in range(i+1,len(l)):
        if l[pos] > l[j]:
            pos = j
            l[i],l[pos]=l[pos],l[i]
print(l)


l = [9,7,3,2,1,0]
for i in range(1,len(l)):
    value = l[i]
    index = i
    while index > 0 and value < l[index - 1]:
        l[index] = l[index - 1]
        index = index - 1
    l[index] = value
print(l)
