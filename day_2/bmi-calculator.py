#Write a program that calculates the Body Mass Index (BMI) from
# a user's weight and height.
#The BMI is a measure of some's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, 
# the short person is usually more overweight.

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#cnverting to int
height = float(height)
weight = float(weight)

bmi = weight / (height * height)

print(int(bmi))
