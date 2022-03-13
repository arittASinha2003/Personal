l = [1,9,7,2,8,5,3]
for i in range(l,len(a)):
    value = a[i]
    index = i
    while index > 0 and value < a[index-1]:
        a[index] = a[index-1]
        index = index-1
    a[index] = value
print(a)
