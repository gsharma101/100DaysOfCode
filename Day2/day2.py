#? Day 2 in python programming
# #! Coding Challange
# #* Don't change the code below
# two_digit_number = input("Type a two digit number: ")
# #* Don't change the code above
# ##########################################
# #!Writing your code below this line
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# print(int(first_digit) + int(second_digit))
# #! Mathematical Operations in python
# add = 3 + 5
# sub = 7 - 3
# mul = 5 * 4
# div = 6 / 3
# print(add)
# print(sub)
# print(mul)
# print(div)
# power = 2 ** 2 # This will do 2^2 = 4
# print(power)
#! Coding Challange 2 calculating the body mass index
# #* Don't change the code below
# height = input("Enter your height in m: ");
# weight = input("Enter your weight in Kg: ");
# #* Don't change the code above
# ############################################
# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)
#! Coding Challange 2 calculating hom many days, weekks and months we have if we live until 90 years
#* Don't change the code below
age = input("What is your current age? ");
#* Don't change the code above
years_left = 90 - int(age)
days = years_left * 365
weeks = years_left * 52
months = years_left * 12
print(f"You have {days} days, {weeks} weeks and {months} months left")

