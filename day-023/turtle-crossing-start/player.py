from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLOR = "black"
SHAPE = "turtle"
SPEED = 20
DIRECTION = 90


class Player(Turtle):

    def __init__(self, color=COLOR, shape=SHAPE,
                 start_pos=STARTING_POSITION, speed=SPEED):
        super().__init__(shape)
        self.start_pos = start_pos
        self.speed = speed
        self.penup()
        self.color(color)
        self.goto(start_pos)
        self.setheading(DIRECTION)
        self.movement = 0

    def update(self):
        self.forward(self.movement)

    def move(self):
        self.movement = self.speed

    def stay(self):
        self.movement = 0

    def restart(self):
        self.goto(self.start_pos)

    def is_finished(self):
        is_finished = self.ycor() > FINISH_LINE_Y
        return is_finished
