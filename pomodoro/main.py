from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECONDS = 60
CHECK_MARK = "✓"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_label["text"] = "Timer"
    canvas.itemconfig(timer_text, text = "00:00")
    start_button["state"] ="normal"
    check_label["text"] = ""
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button["state"] = "disabled"
    global reps
    reps += 1

    if reps % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        seconds = WORK_MIN * SECONDS
    elif reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        seconds = LONG_BREAK_MIN * SECONDS
    else:
        title_label.config(text="Break", fg=PINK)
        seconds = SHORT_BREAK_MIN * SECONDS
    count_down(seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(seconds):
    minutes = math.floor(seconds / SECONDS)
    secs = seconds % SECONDS
    canvas.itemconfig(timer_text, text = f"{minutes:02}:{secs:02}")
    if seconds > 0:
        global timer
        timer = window.after(1000, count_down, seconds - 1)
    else:
        check_label["text"] = CHECK_MARK * (reps // 2)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image= PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text=f"{WORK_MIN}:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW, text="", font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()