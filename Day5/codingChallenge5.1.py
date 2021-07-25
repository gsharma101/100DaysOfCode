# Coding Challenge 5.1
#! Don't change the code below👇
student_height = input("Input a list of student heights ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
#! Don't change the code above👆
total_height = 0
for height in student_height:
    total_height += height
# print(total_height)

number_of_students = 0
for student in student_height:
    number_of_students += 1
# print(number_of_students)

avrage_height = total_height / number_of_students
print(avrage_height)