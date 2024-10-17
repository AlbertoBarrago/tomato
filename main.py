from curses.textpad import Textbox
from idlelib.colorizer import color_config
from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    print("start")
    pass


def reset_timer():
    print("reset")
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.grid_rowconfigure(0, weight=1)

title_label = Label(window, text="Timer", font=(FONT_NAME, 30, "bold"), background=YELLOW, foreground=PINK)
title_label.grid(column=1, row=0, columnspan=2, padx=5, pady=5)

canvas = Canvas(width=200, height=224, bg=YELLOW, borderwidth=0, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2, columnspan=2, pady=20)

button_start = Button(window, text="Start", command=start_timer, highlightthickness=0)
button_start.config(highlightbackground=YELLOW, highlightcolor=YELLOW)
button_start.grid(column=0, row=5, columnspan=2)

mark = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
mark.grid(column=1, row=5, columnspan=2)

button_end = Button(window, text="Reset", command=reset_timer, highlightthickness=0)
button_end.config(highlightbackground=YELLOW, fg=RED, highlightcolor=RED)
button_end.grid(column=2, row=5, columnspan=2)

window.mainloop()
