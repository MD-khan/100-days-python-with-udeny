#!/usr/bin/env python3
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
#student_heights = [180, 124, 165, 173, 189, 169, 146]

student_count = 0
total_height = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])  # converting str to int
    total_height += student_heights[n]
    student_count = n+1

# 🚨 Don't change the code above 👆

# Write your code below this row 👇

print(round(total_height/student_count))
