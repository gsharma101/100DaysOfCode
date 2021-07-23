# Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want> S , M or L ")
add_pepperonie = input("Do you want pepperoni? ")
extra_cheese = input("Do you want extra cheese ")
#* Don't change the code above
bill = 0;
# ! Checking the size of the pizza
if(size == "S"):
    bill += 15
elif(size == "M"):
    bill += 20
elif(size == "L"):
    bill += 25
# ! Checking to add pepperonie
if(add_pepperonie == "Y"):
    if(size == "S"):
        bill += 2
    else:
        bill += 3
# ! Added extra cheese
if( extra_cheese == "Y"):
    bill += 1

print(f"Your final bill is ${bill} ")
