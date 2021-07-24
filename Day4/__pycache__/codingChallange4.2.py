# Coding Challenge
import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# person_who_pay = names[random_choice]
# !Another way of generating random numbers
person_who_pay = random.choice(names)
# !Another way of generating random numbers
print(person_who_pay + "is going to pay the bill")

