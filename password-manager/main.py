import json
from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip


# ---------------------------- SEARCH WEBSITE DETAILS ------------------------------- #

def search_web():
    web_input = web_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No file found.")

    else:
        if web_input in data:
            email = data[web_input]["email"]
            password = data[web_input]["password"]
            messagebox.showinfo(title="Saved Password", message=f"Email: {email}"
                                                                f"\nPassword: {password}")

        else:
            messagebox.showinfo(title="Error", message="No password saved for the entered website.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_let = [choice(letters) for _ in range(randint(8, 10))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]
    password_sym = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_sym + password_num + password_let

    shuffle(password_list)

    password = "".join(password_list)

    if len(pass_entry.get()) == 0:
        pass_entry.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo(title="Message", message="Generated Password copied to clipboard.")
    else:
        pass_entry.delete(0, END)
        pass_entry.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo(title="Message", message="Generated Password copied to clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    web_input = web_entry.get()
    mail_input = mail_entry.get()
    pass_input = pass_entry.get()
    new_data = {
        web_input: {
            "email": mail_input,
            "password": pass_input
        }
    }

    if len(web_input) == 0 or len(pass_input) == 0:
        messagebox.showinfo(title="Oops", message="Dont leave any field empty.")

    else:
        # if is_ok:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Writing new sata to file
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data to new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Writing new sata to file
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)

mail_label = Label(text="Email/Username: ")
mail_label.grid(row=2, column=0)

pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)

web_entry = Entry(width=31)
web_entry.grid(row=1, column=1)
web_entry.focus()

mail_entry = Entry(width=45)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "pmb@gmail.com")

pass_entry = Entry(width=31)
pass_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=10, command=search_web)
search_button.grid(row=1, column=2)

pass_button = Button(text="Get Password", width=10, command=password_gen)
pass_button.grid(row=3, column=2)

save_button = Button(text="Add", width=38, command=save_password)
save_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
