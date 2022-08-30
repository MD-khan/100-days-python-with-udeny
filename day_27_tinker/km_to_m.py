from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile To Km Convert")
window.minsize(width=500, height=500)
window.config(padx=50,pady=50)

#Entries
miles_input = Entry(width=10)
#Add some text to begin with
miles_input.insert(END, int(0))
#Gets text in entry
miles_input.grid(column=1,row=0)

#Labels
label_mile = Label(text="Miles")
label_mile.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_result = Label(text="Result")
label_result.config(text=0)
label_result.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

#Buttons
def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    label_result.config(text = f"{km}")

#calls action() when pressed
button_cal = Button(text="Click Me", command=calculate)
button_cal.grid(column=1, row=2)


window.mainloop()