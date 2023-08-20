# https://docs.python.org/2/library/itertools.html#itertools.combinations

# itertools.combinations(iterable, r)
# This tool returns the  length subsequences of elements from the input iterable.
# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

# Sample Code:
# >>> from itertools import combinations
# >>> 
# >>> print list(combinations('12345',2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
# >>> 
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,4))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

# Task:
# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

# Input Format:
# A single line containing the string S and integer value k separated by a space.

# Constraints:
# 0 < k <= len(S)
# The string contains only UPPERCASE characters.

# Output Format:
# Print the different combinations of string S on separate lines.

# Sample Input:
# HACK 2

# Sample Output:
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK

# Method 1:

from itertools import combinations

inp=input()
strin=sorted(inp.split(' ')[0])
n=int(inp.split(' ')[1])
com=[]

for n in range(1,n+1):
    com+=list(combinations(strin,n))  
for word in com:
    print(''.join(list(word)))

# Method 2:

# from itertools import combinations
# s,k = input().split()
# for i in range(1,int(k)+1):
#     for j in (list(combinations(sorted(s),i))):
#         print ("".join(j))

# Method 3:

# from itertools import combinations
# a,b = input().split()
# l = []
# res =''.join(sorted(a))
# for i in range(1 ,int(b)+1):
#     l=list(combinations(res,i))
#     for j in l:
#         print("".join(j))
