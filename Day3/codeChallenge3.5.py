# Code Challenge 3.5
print("Welcome to the Love calculator: ")
name1 = input("What is your name \n")
name2 = input("What is their name \n")
# ! Changing all the character to lower case
combined_text = name1 + name2
lower_case_string = combined_text.lower()
# ! Counting words in combined letters
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
# !Total the count
true = t + r + u + e
# !Counting the second in the combined letters
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
# !Total the count
love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you got together like coke and mentos.")
elif(love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}") 