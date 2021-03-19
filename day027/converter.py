from tkinter import *

def button_press():
    miles = float(miles_input.get())
    km = miles * 1.6
    converted_label["text"] = str(km)

window = Tk()
window.config(width=300, height=200, padx=10, pady=10)
window.title("Mile to Km Converter")

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

converted_label = Label(text="0")
converted_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=button_press)
button.grid(column=1, row=2)

window.mainloop()