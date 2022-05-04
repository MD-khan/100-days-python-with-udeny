names = ['Monir', "Juma", "Munisa", "Musa"]

import random

student_score = {student:random.randint(1,100) for student in names}

passed_student = { student:score for (student, score) in student_score.items() if score > 60  }

print(passed_student)