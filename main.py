from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="oops", message="Empty fields")
    else:
        is_ok = messagebox.showinfo(title=website, message=f"email:{email}\n "
                                                   f"password:{password}\n are the details correct?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}|{email}|{password}")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ----------------*------------ UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20, bg=YELLOW)

password_image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=password_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="E-mail/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "daniel@gmail.com")

password_entry = Entry(width=29)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3, columnspan=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()