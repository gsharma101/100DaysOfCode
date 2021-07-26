# Coding Challenge 5.2
#! Don't change the code below👇
student_scores = input("Input a list of student heights ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
#! Don't change the code above👆
high_score = 0
for score in student_scores:
    score > high_score
    high_score = score
print(f"The highscore is nthe class is: {high_score}")