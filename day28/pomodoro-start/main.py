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
reps = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def reset_timer():
    canvas.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    checkLabel.config(font=(FONT_NAME, 30), text="", bg=YELLOW, fg=GREEN)


def start():
    global reps
    reps += 1

    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps % 8 == 0:
        heading["text"] = "Break"
        heading["fg"] = RED
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        heading["text"] = "Break"
        heading["fg"] = PINK
    else:
        count_down(work_sec)
        heading["text"] = "Work"
        heading["fg"] = GREEN


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    if count_min <= 9:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = canvas.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(0, work_sessions):
            marks += "✓"
        checkLabel.config(font=(FONT_NAME, 30), text=marks, bg=YELLOW, fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

heading = Label(font=(FONT_NAME, 40), text="Timer", bg=YELLOW, fg=GREEN)
heading.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomadoro_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=pomadoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=2, row=2)

startButton = Button(font=(FONT_NAME, 20), text="Start", bg=YELLOW, fg=RED, highlightthickness=0,
                     command=start)
startButton.grid(column=1, row=3)

resetButton = Button(font=(FONT_NAME, 20), text="Reset", bg=YELLOW, fg=RED, highlightthickness=0,
                     command=reset_timer)
resetButton.grid(column=3, row=3)

checkLabel = Label(font=(FONT_NAME, 30), text="", bg=YELLOW, fg=GREEN)
checkLabel.grid(column=2, row=4)


window.mainloop()
