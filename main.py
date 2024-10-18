from logging.config import stopListening
from tkinter import Tk, Canvas, PhotoImage, Label, Button
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

window = Tk()

STOP_COUNT = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.config(stopListening())
    canvas.itemconfig(timer_text, text="00:00")
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(1 * 60)

# ---------------------------- UI SETUP ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_min, count_sec = handle_time(count_min, count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


def handle_time(count_min, count_sec):
    """
    Handling sec and minutes to print 00:00 in case of < 10 or 0
    :param count_min:
    :param count_sec:
    :return:
    """
    if count_min < 10 or count_min == 0:
        count_min = f"0{count_min}"
    if count_sec < 10 or count_sec == 0:
        count_sec = f"0{count_sec}"
    return count_min, count_sec


window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.grid_rowconfigure(0, weight=1)

title_label = Label(window, text="Timer", font=(FONT_NAME, 30, "bold"), background=YELLOW, foreground=PINK)
title_label.grid(column=1, row=0, columnspan=2, padx=5, pady=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, borderwidth=0, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2, columnspan=2, pady=20)

button_start = Button(window, text="Start", command=lambda: start_timer(), highlightthickness=0)
button_start.config(highlightbackground=YELLOW, highlightcolor=YELLOW)
button_start.grid(column=0, row=5, columnspan=2)

mark = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
mark.grid(column=1, row=5, columnspan=2)

button_end = Button(window, text="Reset", command=lambda: reset_timer(), highlightthickness=0)
button_end.config(highlightbackground=YELLOW, fg=RED, highlightcolor=RED)
button_end.grid(column=2, row=5, columnspan=2)


window.mainloop()
