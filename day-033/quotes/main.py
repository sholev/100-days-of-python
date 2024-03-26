from tkinter import *
from PIL import ImageTk, Image
import requests
import random

NAME = "Frog"
URL = (
    "https://raw.githubusercontent.com/sholev/100-days-of-python/main/day"
    "-032/weekday-quote/quotes.txt")

FONT_SIZE = 20
FONT = ("Arial", FONT_SIZE, "bold")

request = requests.get(URL)
Tk.lines = request.text.split("\n")


def get_quote():
    quote = random.choice(Tk.lines)
    canvas.itemconfig(quote_text, text=quote, font=FONT)
    adjust_font_size()


def adjust_font_size():
    font_size = FONT_SIZE
    bbox = canvas.bbox(quote_text)
    text_height = bbox[3] - bbox[1]
    canvas.itemconfig(quote_text, font=("Arial", font_size, "bold"))
    while 90 + text_height > canvas.winfo_height():
        font_size -= 1
        canvas.itemconfig(quote_text, font=("Arial", font_size, "bold"))
        bbox = canvas.bbox(quote_text)
        text_height = bbox[3] - bbox[1]


window = Tk()
window.title(f"{NAME} Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 200, text=f"{NAME} Quote Goes HERE",
                                width=250, font=FONT)
canvas.grid(row=0, column=0)

image = Image.open("frog.jpg")
image = image.resize((200, 200))
photoImage = ImageTk.PhotoImage(image)
button = Button(image=photoImage, highlightthickness=0, command=get_quote)
button.grid(row=1, column=0)

window.mainloop()
