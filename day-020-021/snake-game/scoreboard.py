from turtle import Turtle

COLOR = "white"
ALIGN = "center"
FONT = ("Arial", 21, "normal")
DISPLAY_TEXT = "Score: {0}"
GAME_OVER_TEXT = "GAME OVER"


class Scoreboard(Turtle):

    def __init__(self, pos=(0, 270)):
        super().__init__()
        self.color(COLOR)
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.display()

    def display(self):
        score_text = DISPLAY_TEXT.format(self.score)
        self.write(score_text, align=ALIGN, font=FONT)

    def game_over(self, pos=(0, 0)):
        self.goto(pos)
        self.write(GAME_OVER_TEXT, align=ALIGN, font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.display()