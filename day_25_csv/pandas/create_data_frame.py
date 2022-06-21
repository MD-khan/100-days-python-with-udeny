#!/usr/bin/env python3

import pandas

# Create a dataframe
data_dict = {
    "students": ['Munisa', 'Musa', 'Monir', 'Jume'],
    "scores": [76, 56, 65,70]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv('student_score.csv')
data.to_html('student_score.html')
