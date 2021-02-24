from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data_dict = pandas.read_csv("data/french_words.csv").to_dict(orient='series')
choice = ""


# -------------------- CHANGE WORDS --------------------#


def start():
    global choice
    choice = random.randint(0, len(data_dict['English']) - 1)
    background.itemconfig(backdrop, image=background_image)
    background.itemconfigure(chosen_word, text=data_dict['English'][choice], fill="white")
    background.itemconfigure(title_text, text="English", fill="white")


def french_word():
    global choice
    background.itemconfig(backdrop, image=frontground_image)
    background.itemconfigure(chosen_word, text=data_dict['French'][choice], fill="black")
    background.itemconfigure(title_text, text="French", fill="black")
    window.after(3000, start)


def is_known():
    data_dict.remove()


# -------------------- UI LAYOUT --------------------#


# display words
window = Tk()
window.title("Flash Card Study Buddy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

background = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
background_image = PhotoImage(file="images/card_back.png")
frontground_image = PhotoImage(file="images/card_front.png")
backdrop = background.create_image(400, 263, image=background_image)
title_text = background.create_text(400, 180, text="Title", font=("Arial", 40, "italic"), fill="white")
chosen_word = background.create_text(400, 300, text="Word", font=("Arial", 60, "bold"), fill="white")
background.grid(column=0, row=0, columnspan=2, rowspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_mark = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=french_word)
wrong_mark.grid(column=0, row=2)

start()

right_image = PhotoImage(file="images/right.png")
right_mark = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=french_word)
right_mark.grid(column=1, row=2)

window.mainloop()
