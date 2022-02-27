#!/usr/bin/env python3
# Python 3.9.6

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    text = text.replace(' ', '')
    cipher_text = ''
    for t in text:
        #index_position = alphabet.index(t) + shift
        cipher_text += alphabet[alphabet.index(t) + shift]
    print(cipher_text)


def decrypt(text, shift):
    text = text.replace(' ', '')
    cipher_text = ''
    for t in text:
        #index_position = alphabet.index(t) + shift
        cipher_text += alphabet[alphabet.index(t) - shift]
    print(cipher_text)


if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)
