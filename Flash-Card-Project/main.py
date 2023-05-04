from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("LangFlash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0)

window.mainloop()
