import tkinter as tk
import pandas
import random

BG_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
FONT_TITLE = (FONT_NAME, 22, "italic")
FONT_WORD = (FONT_NAME, 42, "bold")
TIMING = 3000


class Application:
    def __init__(self):
        self.df = self.load_words()
        self.words = self.df.to_dict(orient="records")
        self.current_word = random.choice(self.words)
        self.current_after = None

        self.window = tk.Tk()
        self.window.title("Flash Card App")
        self.window.config(padx=50, pady=50, bg=BG_COLOR)
        self.window.resizable(False, False)

        self.img_card_front = tk.PhotoImage(file="./images/card_front.png")
        self.img_card_back = tk.PhotoImage(file="./images/card_back.png")
        self.img_check = tk.PhotoImage(file="./images/right.png")
        self.img_x = tk.PhotoImage(file="./images/wrong.png")

        canvas_width = 800
        self.canvas = tk.Canvas(width=canvas_width, height=526, bg=BG_COLOR, highlightthickness=0)
        self.card_img = self.canvas.create_image(400, 263, image=self.img_card_front)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.canvas_title = self.canvas.create_text(canvas_width / 2, 150)
        self.canvas.itemconfig(self.canvas_title, text="", font=FONT_TITLE)
        self.canvas_word = self.canvas.create_text(canvas_width / 2, 250)
        self.canvas.itemconfig(self.canvas_word, text="", font=FONT_WORD)

        self.btn_done = tk.Button(image=self.img_check, highlightthickness=0, bd=0)
        self.btn_done.config(command=self.on_press_check)
        self.btn_done.grid(row=1, column=1)

        self.btn_x = tk.Button(image=self.img_x, highlightthickness=0, bd=0)
        self.btn_x.config(command=self.on_press_x)
        self.btn_x.grid(row=1, column=0)

        self.show_random_word()
        self.window.mainloop()

    @staticmethod
    def load_words():
        try:
            data_frame = pandas.read_csv("./data/words_to_learn.csv")
            if len(data_frame) == 0:
                data_frame = pandas.read_csv("./data/french_words.csv")
        except FileNotFoundError:
            data_frame = pandas.read_csv("./data/french_words.csv")

        return data_frame

    def remove_current_word(self):
        language = list(self.current_word.keys())[0]
        word = self.current_word[language]
        mask = self.df[language] == word
        self.df = self.df[~mask]
        self.df.to_csv("./data/words_to_learn.csv", index=False)

    def start_flip_time(self):
        if self.current_after is not None:
            self.window.after_cancel(self.current_after)
            self.current_after = None
        self.current_after = self.window.after(TIMING, self.flip_word)

    def update_canvas(self, title, word, img, color):
        self.canvas.itemconfig(self.canvas_title, text=title, font=FONT_TITLE, fill=color)
        self.canvas.itemconfig(self.canvas_word, text=word, font=FONT_WORD, fill=color)
        self.canvas.itemconfig(self.card_img, image=img)

    def show_random_word(self):
        self.current_word = random.choice(self.words)
        self.update_canvas("French", self.current_word["French"], self.img_card_front, "black")
        self.start_flip_time()

    def flip_word(self):
        self.update_canvas("English", self.current_word["English"], self.img_card_back, "white")

    def on_press_check(self):
        self.remove_current_word()
        self.show_random_word()

    def on_press_x(self):
        self.show_random_word()


Application()
