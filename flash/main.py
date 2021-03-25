from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
FRENCH = "French"
ENGLISH = "English"
timer = None
current_card ={}

def flip_card():
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(language_text, text=ENGLISH, fill="white")
    canvas.itemconfig(word_text, text=current_card[ENGLISH], fill="white")

def right_pressed():
    global current_card
    french_dict.remove(current_card)
    data = pandas.DataFrame(french_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(french_dict)
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(language_text, text=FRENCH, fill="black")
    canvas.itemconfig(word_text, text=current_card[FRENCH], fill="black")
    timer = window.after(3000, flip_card)

#get a Dataframe
try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("data/french_words.csv")
#each row of DataFrame is a Series. Can process that into dict.
french_dict = data_frame.to_dict(orient="records")

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

language_text = canvas.create_text(400, 150, text='', font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text='', font=(FONT_NAME, 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0, padx=50)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_pressed)
right_button.grid(row=1, column=1, padx=50)

next_card()
window.mainloop()