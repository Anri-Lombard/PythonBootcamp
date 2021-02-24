from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)


def button_clicked():
    answer_label['text'] = int(answer_input.get()) * 1.609344


miles_label = Label(font=("Arial", 20), text="Miles")
miles_label.grid(column=3, row=1, padx=20, pady=(30, 5))
km_label = Label(font=("Arial", 20), text="Km")
km_label.grid(column=3, row=2)
equals_label = Label(font=("Arial", 20), text="is equal to")
equals_label.grid(column=1, row=2, padx=20)
answer_label = Label(font=("Arial", 20), text="0")
answer_label.grid(column=2, row=2)

button = Button(font=("Arial", 20), text="Calculate", command=button_clicked)
button.grid(column=2, row=3, padx=20, pady=(5, 0))

answer_input = Entry(font=("Arial", 20), text="0", width=5)
answer_input.grid(column=2, row=1, pady=(30, 5))

window.mainloop()
