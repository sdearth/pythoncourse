from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [random.choice(letters) for _ in range(0, random.randint(8, 10))]
    pw_symbols = [random.choice(symbols) for _ in range(0, random.randint(2, 4))]
    pw_numbers = [random.choice(numbers) for _ in range(0, random.randint(2, 4))]

    pw_list = pw_letters + pw_symbols + pw_numbers
    random.shuffle(pw_list)
    return("".join(pw_list))

def gen_pressed():
    password = gen_password()
    pw_input.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pressed():
    url = web_input.get()
    id = id_input.get()
    pw = pw_input.get()

    if len(url.strip()) == 0 or len(id.strip()) == 0 or len(pw.strip()) == 0:
        messagebox.showerror(title="Missing Data", message="Please fill in all fields!")
    else:
        is_ok = messagebox.askokcancel(title=url, message="OK to save?")

        if is_ok:
            with open("./data.txt", mode="a") as file:
                file.write(f"{url} | {id} | {pw}\n")
        web_input.delete(0, END)
        web_input.focus()
        pw_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image= PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:", font=(FONT_NAME, 12))
web_label.grid(column=0, row=1)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

id_label = Label(text="Email/Username:", font=(FONT_NAME, 12))
id_label.grid(column=0, row=2)

id_input = Entry(width=35)
id_input.insert(END, "dummy@gmail.com")
id_input.grid(column=1, row=2, columnspan=2)

pw_label = Label(text="Password:", font=(FONT_NAME, 12))
pw_label.grid(column=0, row=3)

pw_input = Entry(width=21, show="*")
pw_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", font=(FONT_NAME, 12), command=gen_pressed)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", font=(FONT_NAME, 12), width=46, command=add_pressed)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()