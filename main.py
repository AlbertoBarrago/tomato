from tkinter import Tk, Canvas, PhotoImage, Label, Button
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
TITLE_PLACEHOLDER = "Start Timer"

reps = 0
STOP_COUNT = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, STOP_COUNT
    STOP_COUNT = True
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text=TITLE_PLACEHOLDER, fg=PINK)
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, STOP_COUNT
    STOP_COUNT = False
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else:
        title_label.config(text="Work Time", fg=GREEN)
        count_down(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global STOP_COUNT
    if STOP_COUNT:
        return

    count_min = math.floor(seconds / 60)
    count_sec = seconds % 60
    count_min, count_sec = handle_time(count_min, count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if seconds > 0:
        window.after(1000, count_down, seconds - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- HELPER FUNCTION ------------------------------- #
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


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(window, text=TITLE_PLACEHOLDER, font=(FONT_NAME, 30, "bold"), background=YELLOW, foreground=PINK)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(window, text="Start", command=start_timer, highlightthickness=0)
button_start.config(highlightbackground=YELLOW, highlightcolor=YELLOW)
button_start.grid(column=0, row=2)

button_reset = Button(window, text="Reset", command=reset_timer, highlightthickness=0)
button_reset.config(highlightbackground=YELLOW, highlightcolor=YELLOW)
button_reset.grid(column=2, row=2)

check_mark = Label(window, text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24))
check_mark.grid(column=1, row=3)


window.mainloop() #Main loop
