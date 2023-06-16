#python 3.7.1
import random

arr = [['◼️','◻️'],
       ['📈','📉'],
       ['📤','📥'],
       ['🧪','🌡️'],
       ['🌸','💮'],
       ['📀','💿'],
       ['💥','🌟'],
       ['🌳','🌲'],
       ['🦋','🐞']]

print('----Themes-----')
for i in range(len(arr)):
  print('Enter %s to %s' %(i, arr[i][0] + arr[i][1]))
print('---------------')

res = input('-----:') or 0
one = arr[int(res)][0]
zero = arr[int(res)][1]

while True:
  a = input("---------[press enter]----------\n")
  if a == '':
    s = ''
    j = 15
    for i in range(256):
      r = random.randint(0, 1)
      if r == 1:
        s+=one
      if r == 0:
        s+=zero
      if i == j:
        s+='\n'
        j+=16.
    print(s)
  else:
    break
