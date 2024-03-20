from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

WHITE = "white"
BLACK = "black"
FONT_NAME = "Courier"
FONT_LABEL = (FONT_NAME, 18, "bold")
FONT_BTN = (FONT_NAME, 12, "bold")
FONT_ENTRY = (FONT_NAME, 14, "bold")


def get_label(row, col, text):
    label = Label(text=text, font=FONT_LABEL, bg=BLACK, fg=WHITE)
    label.grid(row=row, column=col, sticky=E)
    return label


def get_entry(row, col, col_span, width):
    entry = Entry(font=FONT_ENTRY, bg=BLACK, fg=WHITE, width=width)
    entry.grid(row=row, column=col, columnspan=col_span, sticky=W)
    return entry


def get_button(row, col, col_span, width, text, command):
    btn = Button(text=text, font=FONT_BTN, bg=BLACK, fg=WHITE, width=width)
    btn.config(command=command)
    btn.grid(row=row, column=col, columnspan=col_span, sticky=E)
    return btn


def save_to_textfile(website, user, password):
    formatted = f"{website} | {user} | {password}\n"
    with open("data.txt", "a") as data:
        data.write(formatted)


def on_press_add():
    website = website_entry.get()
    user = user_entry.get()
    password = pw_entry.get()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty data",
                            message="Some fields were left empty.")
        return

    formatted = (f"Entry data:\nWebsite: {website}\nUser:{user}\nPassword:"
                 f"{password}")
    if messagebox.askokcancel(title="Confirm save.", message=formatted):
        save_to_textfile(website, user, password)
        website_entry.delete(0, END)
        pw_entry.delete(0, END)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    return "".join(password_list)


def on_press_generate():
    password = generate_password()
    pw_entry.delete(0, END)
    pw_entry.insert(0, password)
    pyperclip.copy(password)


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg=BLACK)
window.resizable(False, False)

canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = get_label(1, 0, "Website:")
website_entry = get_entry(1, 1, 2, 40)
website_entry.focus()
user_label = get_label(2, 0, "Email/Username:")
user_entry = get_entry(2, 1, 2, 40)
user_entry.insert(0, "test@test.com")
pw_label = get_label(3, 0, "Password:")
pw_entry = get_entry(3, 1, 1, 23)
pw_entry.insert(0, generate_password())
generate_btn = get_button(3, 2, 1, 18, "Generate Password", on_press_generate)
add_btn = get_button(4, 1, 2, 44, "Add", on_press_add)

window.mainloop()
