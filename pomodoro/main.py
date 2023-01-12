from tkinter import *
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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=MY_YELLOW)
# hint1 fg = GREEN
# hint2 ✔
# hint3 use grid instead of pack()

# Title label
title_label = Label(text="Pomodoro Timer", fg=MY_GREEN, bg=MY_YELLOW, font=(MY_FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=MY_YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button
start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Checkmark
check_marks = Label(text="✔", fg=MY_GREEN, bg=MY_YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
