#!/usr/bin/env python3

# Adding column in CSV based on custom logic

from csv import writer
from csv import reader


def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)
# Add a column with same values to an existing csv file using generic function & a lambda


default_text = 'Some Text'
# Add column with same text in all rows
add_column_in_csv('input.csv', 'output_2.csv', lambda row,
                  line_num: row.append(default_text))

# Add a column to an existing csv file, based on values from other columns
add_column_in_csv('input.csv', 'output_3.csv', lambda row,
                  line_num: row.append(row[0] + '__' + row[1]))

# Add a list as a column to an existing csv file
list_of_str = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
add_column_in_csv('input.csv', 'output_4.csv', lambda row,
                  line_num: row.append(list_of_str[line_num - 1]))

# Insert a column as second column with same values into an existing csv
# Insert a column in between other columns of the csv file i.e. the second column of csv
add_column_in_csv('input.csv', 'output_5.csv', lambda row,
                  line_num: row.insert(1, row[0] + '__' + row[1]))
print('Add a column with same values to an existing csv file with header')


# Add a column with same values to an existing csv file with header
header_of_new_col = 'Phone'
default_text = '617-866-3824'
# Add the column in csv file with header
add_column_in_csv('input.csv', 'output_6.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))
