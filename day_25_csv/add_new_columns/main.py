#!/usr/bin/env python3

# https://thispointer.com/python-add-a-column-to-an-existing-csv-file/
from csv import writer
from csv import reader

# Add a column with same values to an existing CSV file

default_text = 'Some  useful text'
# Open the input_file in read mode and output_file in write mode
with open('input.csv', 'r') as read_obj, \
        open('output_1.csv', 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
    # Read each row of the input csv file as list
    for row in csv_reader:
        # Append the default text in the row / list
        row.append(default_text)
        # Add the updated row / list to the output file
        csv_writer.writerow(row)


