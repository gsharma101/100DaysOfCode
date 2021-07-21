# !Tip calulator 
note = print(f"Welcome to the tip calculator: ")
bill = float(input(f"What was the total bill: "))
tip = int(input(f"What percentage tip would you like to give? 10, 12, or 15?: "))
people_share = int(input(f"How many people to split the bill: "))
bill_with_tip = tip/100 * bill + bill
print(f"Each person should pay {float(bill_with_tip)}")

