# !Tip calulator 
note = print(f"Welcome to the tip calculator: ")
bill = float(input(f"What was the total bill: "))
tip = int(input(f"What percentage tip would you like to give? 10, 12, or 15?: "))
people_share = int(input(f"How many people to split the bill: "))
bill_with_tip = tip/100 * bill + bill
bill_per_person = bill_with_tip / people_share;
final_amout = round(bill_per_person)
print(f"Each person should pay ${final_amout}:")

