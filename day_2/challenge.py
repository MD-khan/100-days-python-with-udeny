# Write a program that adds the digits in a 2 digit number.
#  e.g. if the input was 12, then the output should be 1 + 2 = 3

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Get the first and second digits using subscripting and conver them to integer
first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])

print(first_num + second_num)