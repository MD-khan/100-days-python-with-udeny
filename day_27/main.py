#!/usr/bin/env python3

from distutils.command.build import build
from tkinter import *

from setuptools import Command

window = Tk()
window.title('GUI Program')
window.minsize(width=500, height=300)

label = Label(text="What is your name", font=("Arial", 24, "bold"))
label.pack()

label["text"] = "New Text"
label.config(text="New Text")

def buttion_cliked():
    # label["text"] = "Got Clicked"
    # #input.get(label)
    text = input.get()
    label.config(text=text)

button = Button(text="Click Me", command=buttion_cliked)
button.pack()

input = Entry(width=10)
input.pack()
print(input.get())


window.mainloop()
