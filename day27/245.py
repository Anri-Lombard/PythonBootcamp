from tkinter import *

window = Tk()
window.title("My first Python GUI")
window.minsize(width=600, height=500)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=2, row=1)
my_label["text"] = "My Label"


def button_clicked():
    my_button["text"] = "clicked"
    my_label["text"] = input.get()


my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=2, row=2)

input = Entry(width=10)
input.grid(row=3, column=2)









window.mainloop()
