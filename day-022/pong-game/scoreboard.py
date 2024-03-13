from turtle import Turtle

COLOR = "white"
FONT = ("Courier", 60, "bold")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self, color=COLOR, pos_l=(-100, 200), pos_r=(100, 200)):
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.l_pos = pos_l
        self.r_pos = pos_r
        self.write_score(pos_l, self.l_score)
        self.write_score(pos_r, self.r_score)

    def write_score(self, pos, score):
        self.goto(pos)
        self.write(score, align=ALIGN, font=FONT)

    def r_increment(self):
        self.clear()
        self.r_score += 1
        self.write_score(self.r_pos, self.r_score)
        self.write_score(self.l_pos, self.l_score)

    def l_increment(self):
        self.clear()
        self.l_score += 1
        self.write_score(self.l_pos, self.l_score)
        self.write_score(self.r_pos, self.r_score)
