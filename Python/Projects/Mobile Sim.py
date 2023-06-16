#Import
import time
import datetime
import random
import calendar
x = datetime.date.today()

#Welcome
print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
print("🌟WELCOME TO MOBILE PHONE SIMULATOR🌟")
print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
time.sleep(1)
name = input("\nENTER YOUR NAME: ")
print(f"\nHELLO {name.upper()}")
time.sleep(0.5)
print(f"DATE - {x}")
time.sleep(0.5)
print("BATTERY POWER - 100%")
time.sleep(0.5)

#Apps
while 1 > 0:
  time.sleep(1)
  print("\n___APPS___")
  time.sleep(0.5)
  print("TYPE 1 TO CHAT.")
  time.sleep(0.5)
  print("TYPE 2 TO CALL.")
  time.sleep(0.5)
  print("TYPE 3 FOR CONTACTS.")
  time.sleep(0.5)
  print("TYPE 4 FOR MESSAGES.")
  time.sleep(0.5)
  print("TYPE 5 FOR CALENDAR.")
  time.sleep(0.5)
  print("TYPE 6 FOR CALCULATOR.")
  time.sleep(0.5)
  print("TYPE 7 FOR AGE CALCULATOR.")
  time.sleep(0.6)
  print("TYPE 8 FOR RANDOM NUMBER GENERATOR.")
  time.sleep(0.7)
  print("TYPE 9 FOR GAMES.")
  time.sleep(0.5)
  option = int(input("CHOOSE AN OPTION: "))
  time.sleep(0.5)

  #Games
  if option == 9:
    print("\n___GAMES___")
    time.sleep(0.5)
    print("TYPE 1 FOR NUMBER GUESSING GAME.")
    time.sleep(0.5)
    print("TYPE 2 TO DOWNLOAD OTHER GAMES.")
    time.sleep(0.5)
    print("TYPE 3 TO GO BACK TO APPS.")
    time.sleep(0.5)
    option0 = int(input("CHOOSE AN OPTION: "))
    time.sleep(0.5)
    if option0 == 2:
      print("\nSORRY, YOU HAVE NO ACCOUNT BALANCE.")
    if option0 == 1:
      print("\n___NUMBER GUESSING GAME___")
      guess = 1
      win_number = random.randrange(1,100)
      number = int(input("GUESS A NUMBER BETWEEN 1 TO 100: "))
      while number != win_number:
        if number < win_number:
          guess += 1
          print("\nWRONG GUESS! YOU HAVE TO GUESS HIGHER.")
          time.sleep(0.5)
          number = int(input("GUESS A NUMBER BETWEEN 1 TO 100: "))
        if number > win_number:
          guess += 1
          print("\nWRONG GUESS! YOU HAVE TO GUESS LOWER.")
          time.sleep(0.5)
          number = int(input("GUESS A NUMBER BETWEEN 1 TO 100: "))
      print("\n👏👌👍CONGRATULATIONS👍👌👏")
      time.sleep(0.5)
      print(f"YOU HAVE GUESSED CORRECTLY IN {guess} TIMES.")

  #Random Number Generator
  if option == 8:
    print("\n___RANDOM NUMBER GENERATOR___")
    time.sleep(0.5)
    n1 = int(input("ENTER THE FIRST/STARTING NUMBER: "))
    n2 = int(input("ENTER THE LAST/ENDING NUMBER: "))
    n3 = random.randrange(n1,n2)
    time.sleep(0.5)
    print(f"\nTHE RANDOM NUMBER IS {n3}")

  #Age Calculator
  if option == 7:
    print("\n___AGE CALCULATOR___")
    time.sleep(0.5)
    year1 = int(input("ENTER THE PRESENT YEAR: "))
    year2 = int(input("ENTER THE YEAR OF ITS BIRTH OR BEGINNING: "))
    age = year1 - year2
    time.sleep(0.5)
    print(f"\nIN YEARS, THE AGE IS {age} YEARS.")
    time.sleep(1)
    print(f"IN MONTHS, THE AGE IS {age*12} MONTHS.")
    time.sleep(1)
    print(f"IN DAYS, THE AGE IS {age*365} DAYS.")
    time.sleep(1)
    print(f"IN HOURS, THE AGE IS {age*365*24} HOURS.")
    time.sleep(1)
    print(f"IN MINUTES, THE AGE IS {age*365*24*60} MINUTES.")
    time.sleep(1)
    print(f"IN SECONDS, THE AGE IS {age*365*24*60*60} SECONDS.")

  #Calculator
  if option == 6:
    print("\n___CALCULATOR___")
    time.sleep(0.5)
    num1 = int(input("ENTER THE FIRST NUMBER: "))
    num2 = int(input("ENTER THE SECOND NUMBER: "))
    time.sleep(0.5)
    print("\nTYPE 1 TO ADD (+) THEM.")
    time.sleep(0.5)
    print("TYPE 2 TO SUBTRACT (-) THEM.")
    time.sleep(0.5)
    print("TYPE 3 TO MULTIPLY (×) THEM.")
    time.sleep(0.5)
    print("TYPE 4 TO DIVIDE (÷) THEM.")
    time.sleep(0.5)
    option1 = int(input("CHOOSE AN OPTION: "))
    time.sleep(0.5)
    print("")
    if option1 == 1:
      print(f"SUM = {num1+num2}")
    if option1 == 2:
      print(f"DIFFERENCE = {num1-num2}")
    if option1 == 3:
      print(f"PRODUCT = {num1*num2}")
    if option1 == 4:
      print(f"QUOTIENT = {num1/num2}")

  #Calendar
  if option == 5:
    print("\n___CALENDAR___")
    time.sleep(0.5)
    print("TYPE 1 FOR WHOLE YEAR CALENDAR.")
    time.sleep(0.5)
    print("TYPE 2 FOR ONLY ONE MONTH CALENDAR.")
    time.sleep(0.5)
    option2 = int(input("CHOOSE AN OPTION: "))
    time.sleep(0.5)
    print("")
    if option2 == 1:
      year = int(input("ENTER THE YEAR: "))
      time.sleep(0.5)
      print(f"\nCALENDAR FOR THE YEAR {year}")
      print("")
      print(calendar.month(year,1))
      time.sleep(1)
      print(calendar.month(year,2))
      time.sleep(1)
      print(calendar.month(year,3))
      time.sleep(1)
      print(calendar.month(year,4))
      time.sleep(1)
      print(calendar.month(year,5))
      time.sleep(1)
      print(calendar.month(year,6))
      time.sleep(1)
      print(calendar.month(year,7))
      time.sleep(1)
      print(calendar.month(year,8))
      time.sleep(1)
      print(calendar.month(year,9))
      time.sleep(1)
      print(calendar.month(year,10))
      time.sleep(1)
      print(calendar.month(year,11))
      time.sleep(1)
      print(calendar.month(year,12))
    if option2 == 2:
      year2 = int(input("ENTER THE YEAR: "))
      month = int(input("ENTER THE MONTH: "))
      print("")
      time.sleep(0.5)
      print(calendar.month(year2,month))

  #Messages
  if option == 4:
    print("\n___📨MESSAGES📨___")
    time.sleep(0.5)
    print("\nJIO- Your plan has expired.")
    print("     Recharge your phone...")
    time.sleep(0.5)
    print("___________________________")
    time.sleep(0.5)
    print("\nJIO- You have exhausted your")
    print("     daily high speed data..")
    time.sleep(0.5)
    print("____________________________")

  #Contacts
  if option == 3:
    print("\n___CONTACTS___")
    time.sleep(0.5)
    print("TYPE 1 TO ADD NEW CONTACT.")
    time.sleep(0.5)
    print("TYPE 2 TO SEE CONTACTS.")
    time.sleep(0.5)
    option3 = int(input("CHOOSE AN OPTION: "))
    time.sleep(0.5)
    print("")
    if option3 == 1:
      name2 = input("TYPE THE NAME: ")
      nu = int(input("TYPE THE PHONE NUMBER: "))
      time.sleep(0.5)
      print(f"\n👤 {name2}")
      print(f"{nu}")
      time.sleep(0.5)
      print("\nNOTE: NEW CONTACTS TAKE TIME TO BE ADDED.")
    if option3 == 2:
      print("1. MY LOVE")
      print("   8908904190")
      time.sleep(0.5)
      print("\n2. BEST BUDDY")
      print("   8249457627")

  #Call
  if option == 2:
    print("\n___📞CALL📞___")
    time.sleep(0.5)
    print("TYPE 1 TO SEE CALL LOGS.")
    time.sleep(0.5)
    print("TYPE 2 TO CALL ANYONE.")
    time.sleep(0.5)
    option4 = int(input("CHOOSE AN OPTION: "))
    time.sleep(0.5)
    print("")
    if option4 == 1:
      print("YESTERDAY 5 AM: MY LOVE [8908904190]")
      time.sleep(0.5)
      print("YESTERDAY 5 PM: BEST BUDDY [8249457627]")
    if option4 == 2:
      print("SORRY, YOU HAVE NO ACCOUNT BALANCE.")

  #Chat
  if option == 1:
    print("\n___CHAT___")
    time.sleep(0.5)
    print("\nTYPE 1 TO CHAT WITH 'MY LOVE'")
    time.sleep(0.5)
    print("TYPE 2 TO CHAT WITH 'BEST BUDDY'")
    time.sleep(0.5)
    option5 = int(input("CHOOSE A CONTACT TO CHAT:"))
    time.sleep(0.5)
    print("")
    if option5 == 1:
      print("WRITE")
      input("YOUR MESSAGE: ")
      time.sleep(0.5)
      print("\nMY LOVE: Sorry, I am busy with a threesome.")
      print("         Talk with you later.")
    if option5 == 2:
      print("HELLO... HOW ARE YOU?")
      time.sleep(0.5)
      print("WRITE")
      input("YOUR MESSAGE: ")
      time.sleep(0.5)
      print("\nTHANKS FOR YOUR TIME.")
      time.sleep(1)
      print("PLEASE TAP THE STAR 🌟 IF YOU APPRECIATE MY WORK.")
      time.sleep(1.5)
      print("THIS PROGRAMME IS UNDER DEVELOPMENT AND NEED YOUR SUGGESTIONS.")
      time.sleep(1.5)
      print("SUGGEST CHANGES IN COMMENT SECTION IF ANY.")
      time.sleep(1.5)
      print("PLEASE VISIT MY PROFILE FOR OTHER AMAZING PROGRAMMES.")
