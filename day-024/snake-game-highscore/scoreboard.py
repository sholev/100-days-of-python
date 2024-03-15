from turtle import Turtle

COLOR = "white"
ALIGN = "center"
FONT = ("Arial", 21, "normal")
DISPLAY_TEXT = "Score: {0} | Highscore: {1}"
GAME_OVER_TEXT = "GAME OVER"
FILE = "data.txt"


class Scoreboard(Turtle):

    def __init__(self, pos=(0, 270)):
        super().__init__()
        self.color(COLOR)
        self.score = 0
        with open(FILE) as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.display()

    def display(self):
        self.clear()
        score_text = DISPLAY_TEXT.format(self.score, self.highscore)
        self.write(score_text, align=ALIGN, font=FONT)

    def write_game_over(self, pos=(0, 0)):
        self.goto(pos)
        self.write(GAME_OVER_TEXT, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(FILE, mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.display()

    def increment(self):
        self.score += 1
        self.display()
