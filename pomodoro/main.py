from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
MY_GREEN = "#125c13"
YELLOW = "#f7f5dd"
MY_YELLOW = "#fffad7"
FONT_NAME = "Courier"
MY_FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=MY_YELLOW)


# Title label
title_label = Label(text="Pomodoro Timer", fg=MY_GREEN, bg=MY_YELLOW, font=(MY_FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=MY_YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Checkmark
check_marks = Label(text="✔", fg=MY_GREEN, bg=MY_YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
