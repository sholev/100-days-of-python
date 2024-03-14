from turtle import Turtle

FONT = ("Courier", 24, "bold")
COLOR = "black"
ALIGN = "center"
FORMAT = "Level: {0}"
GAME_OVER = "GAME OVER"


class Scoreboard(Turtle):

    def __init__(self, color=COLOR, pos=(-0, 0)):
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.level = 0
        self.pos = pos
        self.write_level(pos, self.level)

    def write_level(self, pos, level):
        self.goto(pos)
        self.write(FORMAT.format(level), align=ALIGN, font=FONT)

    def increment(self):
        self.clear()
        self.level += 1
        self.write_level(self.pos, self.level)

    def write_game_over(self):
        self.goto(0, 0)
        self.write(GAME_OVER, align=ALIGN, font=FONT)
