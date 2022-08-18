#!/usr/bin/env python3
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# open the file
with open('./Input/Letters/test.txt') as file:
    email_format = file.readlines()

#print(''.join(email_format).replace("[name]", "monir"))

# read the name file and make a list
with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()


# write a file with the name
for name in names:
    print(name.strip())
    with open ('./Output/ReadyToSend/'+name.lower().strip()+'.txt', 'w') as file:
        k = file.write(''.join(email_format).replace("[name]", name.strip()))




