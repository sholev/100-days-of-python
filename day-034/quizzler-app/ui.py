from tkinter import *
from quiz_brain import QuizBrain

COLOR_BG = "#375362"
COLOR_FG = "white"
COLOR_T = "green"
COLOR_X = "red"
FONT = ("Arial", 16, "italic")
FEEDBACK_MS = 1000


class QuizUi:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_bran = quiz_brain
        self.is_feedback = False

        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(background=COLOR_BG, padx=20, pady=20)

        self.score_text = Label(text="Score: 0", font=FONT, bg=COLOR_BG,
                                fg=COLOR_FG)
        self.score_text.grid(row=0, column=1)

        self.q_num_text = Label(text="Q: 0", font=FONT, bg=COLOR_BG,
                                fg=COLOR_FG)
        self.q_num_text.grid(row=0, column=0)

        self.canvas = Canvas(width=300, height=250, bg=COLOR_FG)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        self.q_text = self.canvas.create_text(150, 125, width=280)
        self.canvas.itemconfig(self.q_text, font=FONT, fill=COLOR_BG)
        self.quiz_next_question()

        self.img_true = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=self.img_true, bd=0)
        self.btn_true.config(command=self.on_press_true, highlightthickness=0)
        self.btn_true.grid(row=2, column=0)

        self.img_false = PhotoImage(file="images/false.png")
        self.btn_false = Button(image=self.img_false, bd=0)
        self.btn_false.config(command=self.on_press_false, highlightthickness=0)
        self.btn_false.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop()

    def quiz_next_question(self):
        if self.quiz_bran.still_has_questions():
            question = self.quiz_bran.next_question()
            question_str = question[-1]
            question_num = question[0]
            self.q_num_text.config(text=f"Q: {question_num}")
            self.canvas.itemconfig(self.q_text, text=question_str)
        else:
            self.canvas.itemconfig(self.q_text, text="Quiz completed.")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def on_press_true(self):
        if self.is_feedback:
            return

        is_correct = self.quiz_bran.check_answer("True")
        self.give_feedback(is_correct)

    def on_press_false(self):
        if self.is_feedback:
            return

        is_correct = self.quiz_bran.check_answer("False")
        self.give_feedback(is_correct)

    def on_feedback_finish(self):
        self.canvas.config(background=COLOR_FG)
        self.quiz_next_question()
        self.is_feedback = False

    def give_feedback(self, answer):
        if self.is_feedback:
            return

        color = COLOR_T if answer else COLOR_X
        self.canvas.config(background=color)
        self.window.after(FEEDBACK_MS, self.on_feedback_finish)
        self.score_text.config(text=f"Score: {self.quiz_bran.score}")
        self.is_feedback = True
