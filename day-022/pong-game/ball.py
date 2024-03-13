import math
from random import choice
from turtle import Turtle

COLOR = "white"
SHAPE = "circle"
COLLIDE_DISTANCE = 20
SIZE = 1


class Ball(Turtle):

    def __init__(self, move_speed=20):
        super().__init__(SHAPE)
        self.penup()
        self.shapesize(SIZE, SIZE)
        self.color(COLOR)
        self.velocity = [0, 0]
        self.move_speed = move_speed
        self.randomize_velocity(move_speed)

    def restart(self, speed):
        self.move_speed = speed
        self.goto((0, 0))
        self.randomize_velocity(speed)

    def randomize_velocity(self, move_speed):
        x = choice([-move_speed, move_speed])
        y = choice([-move_speed, move_speed])
        self.velocity = [x, y]

    def move(self):
        x = self.xcor() + self.velocity[0]
        y = self.ycor() + self.velocity[1]
        self.goto(x, y)

    def check_collision(self, objects):
        for obj in objects:
            if self.distance(obj.xcor(), obj.ycor()) < COLLIDE_DISTANCE:
                return obj

    def bounce_y(self):
        self.velocity[1] *= -1

    def bounce_x(self, increase=0):
        self.velocity[0] *= -1
        if self.velocity[0] > 0 and increase > 0:
            self.velocity[0] += increase
        elif self.velocity[0] < 0 < increase:
            self.velocity[0] -= increase
