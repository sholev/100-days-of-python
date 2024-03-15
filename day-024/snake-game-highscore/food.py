import random
from turtle import Turtle

COLOR = "white"
SHAPE = "circle"
SPEED = "fastest"
SIZE = 1


class Food(Turtle):

    def __init__(self, max_pos=(280, 280)):
        super().__init__(SHAPE)
        self.penup()
        self.shapesize(SIZE, SIZE)
        self.color(COLOR)
        self.speed(SPEED)
        self.refresh(max_pos)

    def refresh(self, max_pos=(280, 280)):
        x = random.randint(-max_pos[0], max_pos[0])
        x = x - (x % 20)
        y = random.randint(-max_pos[1], max_pos[1])
        x = y - (y % 20)
        self.goto(x, y)
