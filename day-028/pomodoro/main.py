import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "white"
FONT_NAME = "Courier"
FONT = (FONT_NAME, 35, "bold")
FONT_BTN = (FONT_NAME, 14, "bold")
FONT_CHECK = (FONT_NAME, 22, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps_time = [WORK_MIN, SHORT_BREAK_MIN] * 3 + [WORK_MIN, LONG_BREAK_MIN]
reps_label = ["\nWork", "Short\nbreak"] * 3 + ["\nWork", "Long\nbreak"]
reps_color = [GREEN, PINK] * 3 + [GREEN, RED]
reps_checkmarks = [" ", "✓", "✓", "✓✓", "✓✓", "✓✓✓", "✓✓✓", "✓✓✓✓"]
reps = 0
current_job = None


def timer_reset():
    stop_previous()
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="\nTimer", fg=GREEN)
    update_checkmarks(reps)
    pass


def timer_start():
    stop_previous()
    global reps
    seconds = reps_time[reps % len(reps_time)] * 60
    update_timer(10, seconds, timer_start)
    update_title(reps)
    update_checkmarks(reps)
    reps += 1


def stop_previous():
    global current_job
    if current_job is not None:
        window.after_cancel(current_job)


def update_timer(ms, count, on_finish=None):
    minutes = math.floor(count / 60)
    seconds = count % 60
    text = f"{minutes}:{seconds if seconds > 9 else f"0{seconds}"}"
    canvas.itemconfig(timer_text, text=text)
    if count > 0:
        global current_job
        current_job = window.after(ms, update_timer, ms, count - 1, on_finish)
    elif on_finish is not None:
        on_finish()


def update_title(index):
    text = reps_label[index % len(reps_label)]
    color = reps_color[index % len(reps_color)]
    title_label.config(text=text, fg=color)


def update_checkmarks(index):
    text = reps_checkmarks[index % len(reps_checkmarks)]
    check_labels.config(text=text)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=WHITE, font=FONT)
canvas.grid(row=1, column=1)

title_label = Label(text="\nTimer")
title_label.config(fg=GREEN, bg=YELLOW, font=FONT)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", font=FONT_BTN, highlightthickness=0)
start_button.config(command=timer_start)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", font=FONT_BTN, highlightthickness=0)
reset_button.config(command=timer_reset)
reset_button.grid(row=3, column=3)

check_labels = Label(text=" ")
check_labels.config(fg=GREEN, bg=YELLOW, font=FONT_CHECK)
check_labels.grid(row=4, column=1)

window.mainloop()
