# coding Challenge 4.3
# ! Dont change the code below 👇
row1 = ['⬜','⬜','⬜']
row2 = ['⬜','⬜','⬜']
row3 = ['⬜','⬜','⬜']
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to put the treasure ")
# ! Dont change the code above 👆

# ?Write your code below this code
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
