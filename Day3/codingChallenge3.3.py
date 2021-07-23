# coding challenge 3.3
# *Don't change the code below
year = int(input("Which year do you want to check "))
# * Don't change the code above

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a leap year")
        else:
            print("Not a leap year")
    else:
        print("Yes a leap year")
else:
     print("Not a leap year")