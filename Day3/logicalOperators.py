# Logical Operators in python
height = int(input("Enter your height "))
age = int(input("Enter your age "))
ticket = 0
# ! Checking your height
if height > 120:
    print("You can ride")
else:
    print("You can't ride")

if age < 12:
    ticket = 5
elif age <= 18:
    ticket = 7
elif age >=45 and age <= 55:
    ticket = 0
else:
    ticket = 12

wants_photo = input("Do you want a photo taken? Y or N ")
if wants_photo == "Y":
    ticket += 3;

print(f"Your final bill is ${ticket}")