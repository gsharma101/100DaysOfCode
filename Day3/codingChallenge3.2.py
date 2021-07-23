# coding challenge 3.2
#*Don't change the code below
height = float(input("Enter your height in m: "));
weight = float(input("Enter your weight in Kg: "));
#* Don't change the code above

bmi = weight / height ** 2

if bmi < 18.5:
    print*(f"Your BMI is {bmi}. You are underweight")
elif bmi < 25:
    print*(f"Your BMI is {bmi}. You are normal weight") 
elif bmi < 30:
    print*(f"Your BMI is {bmi}. You are overweight") 
elif bmi < 35:
    print*(f"Your BMI is {bmi}. You are obese")
else:
    print*(f"Your BMI is {bmi}. You are clinically obese") 