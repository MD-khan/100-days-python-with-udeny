#!/usr/bin/env python3

import tkinter


window = tkinter.Tk()
window.title('GUI Program')
window.minsize(width=500, height=300)

label = tkinter.Label(text="Name",font=("Arial", 24, "bold"))
label.pack()