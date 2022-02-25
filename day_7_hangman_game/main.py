#!/usr/bin/env python3
# Python 3.9.6


from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list
import random

print(logo)

# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# randomly choose a word from the word list
machine_pick_word = random.choice(word_list).lower()

display = []
# making slots to put the letter
# We creating slot putnong the _
for under_score in range(len(machine_pick_word)):
    display += "_"


end_game = False
while end_game != True:
    # Ask user to guess the word
    guess = input("Guess a letter: ")

    if guess in display:
        print(f"You already guessed{guess}")

    # Check guessed letter
    for position in range(len(machine_pick_word)):
        letter = machine_pick_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in machine_pick_word:
        print(f"You guessed {guess} that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_game = True
            print(f"Word was {machine_pick_word.upper()}")
    # print(display)
    # Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

    if "_" not in display:
        print("Congratulations!")
        end_game = True

    print(stages[lives])
