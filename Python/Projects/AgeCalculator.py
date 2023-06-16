import sys
print("What is the date today?\n\n")

a = int(input("Enter the date of the month: "))
if (a > 31):
  print("***INVALID DATE OF THE MONTH***")
  sys.exit()

b = int(input("Enter the month of the year (in number): "))
if (b > 12):
  print("***INVALID MONTH OF THE YEAR***")
  sys.exit()

c = int(input("Enter the year: "))
if (c > 2100):
  print("***INVALID YEAR***")
  sys.exit()

print("\n\nWhat is your date of birth?\n\n")

d = int(input("Enter the date of the month: "))
if (d > 31):
    print("***INVALID DATE OF THE MONTH***")
    sys.exit()

e = int(input("Enter the month of the year (in number): "))
if (e > 12):
        print("***INVALID MONTH OF THE YEAR***")
        sys.exit()

f = int(input("Enter the year: "))
if (f > 2100):
        print("***INVALID YEAR***")
        sys.exit()

# Now we start calculating

print("\nYou've lived for: ")
print(" ")

# First we calculate the years


if (b < e):
  g = int(c) - int(f) - 1

if (b == e):
  
  if (a > d):
    g = int(c) - int(f)
    
  elif (a == d):
    print("Happy Birthday!")
    g = int(c) - int(f)
    
  elif (a < d):
    g = int(c) - int(f) - 1
    
if (b > e):
  g = int(c) - int(f)

print(str(g) + " years")


# Then we calculate the months


if (g == int(c) - int(f)):
  
    h = int(b) - int(e)
    
if (g == int(c) - int(f) - 1):
  
  if (a >= d):
    h = int(b) + 12 - int(e)
    
  elif (a < d):
    h = int(b) + 11 - int(e)
  
print(str(h) + " months")


# Finally we calculate the days


if (a >= d):
  
  i = int(a) - int(d)
  
elif (a < d):
  
  i = int(a) + 30.4375 - int(d)
  
print(str(int(i)) + " days")


print("")
print("or: ")
print("")
j = g * 365.25 + h * 30.4375 + i
print(str(int(j)) + " days")

print("")
k = j * 24
print(str(int(k)) + " hours")

print("")
l = k * 60
print(str(int(l)) + " minutes")

print("")
m = l * 60
print(str(int(m)) + " seconds")
