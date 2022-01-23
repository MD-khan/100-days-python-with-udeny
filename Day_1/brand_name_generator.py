#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
print("Welcome to the Brand Name Generator")

city_name = input("What is the name of city you  grew up?\n")
print("your city name is : "+ city_name)
pet_name = input("What is the name of your pet\n")
print("your pet name is : "+ pet_name)

brand_name = city_name +" "+ pet_name
print("your brand name could be: " + brand_name)
