from tkinter import *
from tkmacosx import Button
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data_results = data[website]
    except KeyError:
        messagebox.showerror(title="Oops", message="There seems to be no match. You could try another website.")
    else:
        messagebox.showinfo(title="Results", message=f"Email: {data_results['email']}\nPassword: "
                                                     f"{data_results['password']}")
    website_input.delete(0, END)
    website_input.focus()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
        website_input.focus()
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"You entered:\nemail: {email}\npassword: {password}\n "
                                               f"for website '{website}'"
                                               f"\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as password_file:
                    # reading old docs.
                    data = json.load(password_file)
                    # updating old docs.
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as password_file:
                    json.dump(new_data, password_file, indent=4)
            else:
                with open("data.json", "w") as password_file:
                    # saving updated docs.
                    json.dump(data, password_file, indent=4)

            messagebox.showinfo(title="Success!", message="Successfully saved!")
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()
        else:
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.focus()
website_input.config(width=21)
website_input.grid(column=1, row=1)

search_button = Button(text="Search", width=125, command=search)
search_button.grid(column=2, row=1)

# email/username
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_input = Entry()
email_username_input.insert(0, "anri.m.lombard@gmail.com")
email_username_input.config(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)

# password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry()
password_input.config(width=21)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width=125, command=generate_password)
generate_password_button.grid(column=2, row=3)

# add
add_button = Button(text="Add", command=save, width=322)
add_button.grid(column=1, row=4, columnspan=36)

window.mainloop()
