import time
a=int(input("Enter number of seconds: "))
while a!=0:
  print(str(a) + "  seconds remaining")
  time.sleep(1)
  a=a-1
print ("The time is up!!! ")
time.sleep(1)
