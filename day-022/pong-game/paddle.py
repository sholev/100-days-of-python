from turtle import Turtle

START_POS = ((0, 0), (-20, 0), (-40, 0))
COLOR = "white"
SHAPE = "square"
SPEED = 20
SIZE = 20


class Paddle:

    def __init__(self, color=COLOR, shape=SHAPE, start_pos=START_POS,
                 move_speed=SPEED, size=SIZE):
        self.segments = []
        for pos in start_pos:
            self.add_segment(pos, color, shape, size)
        self.movement = 0
        self.speed_up = move_speed
        self.speed_down = -move_speed

    def add_segment(self, pos, color=COLOR, shape=SHAPE, size=SIZE):
        box = Turtle(shape)
        box.penup()
        box.color(color)
        box.shapesize(size)
        box.goto(pos)
        self.segments.append(box)

    def move(self):
        for segment in self.segments:
            x = segment.xcor()
            y = segment.ycor() + self.movement
            segment.goto(x, y)

    def stay(self):
        self.movement = 0

    def up(self):
        self.movement = self.speed_up

    def down(self):
        self.movement = self.speed_down
