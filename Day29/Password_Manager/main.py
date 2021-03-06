from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get().capitalize()
    username = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Blank Fields", message="One or more fields are empty.")
    else:
        try:
            with open("Day29/Password_Manager/data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        except json.JSONDecodeError:
            data = new_data
        finally:
            with open("Day29/Password_Manager/data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        entry_website.delete(0, END)
        entry_password.delete(0, END)
        entry_website.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_website.get().capitalize()

    try:
        with open("Day29/Password_Manager/data.json", mode="r") as data_file:
            data = json.load(data_file)
            if website in data:
                username = data[website]["username"]
                password = data[website]["password"]
                pyperclip.copy(password)
                messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}\n\nPassword has been copied to clipboard.")
            else:
                messagebox.showinfo(title="Not Found", message=f"No data found for this website: '{website}'")
    except FileNotFoundError:
        messagebox.showerror(title="Keystore Error", message="Keystore file does not exist")
    except json.JSONDecodeError:
        messagebox.showerror(title="Empty Keystore", message="Keystore file is empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="Day29/Password_Manager/logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:", width=15, anchor="e")
label_username = Label(text="Email / Username:", width=15, anchor="e")
label_password = Label(text="Password:", width=15, anchor="e")

# Entries
entry_website = Entry(width=35)
entry_username = Entry(width=54)
entry_password = Entry(width=35)

# Buttons
button_search = Button(text="Search", width=14, command=find_password)
button_generate = Button(text="Generate Password", command=generate_password)
button_add = Button(text="Add", width=45, command=save)

# Layout
label_website.grid(row=1, column=0)
entry_website.grid(row=1, column=1)
entry_website.focus()
button_search.grid(row=1, column=2)
label_username.grid(row=2, column=0)
entry_username.grid(row=2, column=1, columnspan=2)
entry_username.insert(0, "mail@example.com")
label_password.grid(row=3, column=0)
entry_password.grid(row=3, column=1)
button_generate.grid(row=3, column=2)
button_add.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()