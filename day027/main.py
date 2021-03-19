from tkinter import *

def button_clicked():
    #my_label["text"] = input.get()
    label_string.set(input.get())

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

label_string = StringVar(window)
label_string.set("Label")

#Label
#whenever StringVar label_string changes, the label value will update
my_label = Label(textvariable=label_string, font=("Arial", 24, "bold"))

#packer is a geometry management system for laying out components
my_label.grid(column=0,row=0)

# ways to change properties
#my_label["text"] = "New Text"
#my_label.config(text="Some text")

input = Entry(width=10)
input.grid(column=1,row=1)

button = Button(text="Click me", command=button_clicked)
button.grid(column=2,row=0)
# main execution loop
window.mainloop()
