#!/usr/bin/env python3
# Python 3.9.6

# Highest Score
#student_scores = input("Input a list of student scores ").split()
student_scores = [78, 65, 89, 86, 55, 91, 64, 89, 99]
highest_score = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if highest_score < student_scores[n]:
        highest_score = student_scores[n]
print(highest_score)
