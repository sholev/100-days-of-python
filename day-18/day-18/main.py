from random import *
from turtle import Turtle as Trtl, Screen


def random_color():
    color = (random(), random(), random())
    return color


turtle = Trtl()
scale = 0.7

turtle.shape("turtle")
turtle.color("green")
turtle.pensize(3)
turtle.speed("fastest")

turtle.penup()
turtle.left(90)
turtle.forward(400)
turtle.right(90)
turtle.pendown()

for _ in range(4):
    turtle.forward(75 * scale)
    turtle.right(90)

turtle.left(90)
for _ in range(4):
    for _ in range(5):
        turtle.forward(7.5 * scale)
        turtle.penup()
        turtle.forward(7.5 * scale)
        turtle.pendown()
    turtle.left(90)


turtle.penup()
turtle.forward(100 * scale)
turtle.left(90)
turtle.forward(200 * scale)
turtle.left(180)
turtle.pendown()


for r in range(3, 11):
    turtle.color(random_color())
    for _ in range(r):
        turtle.forward(400 * scale)
        turtle.right(360 / r)


turtle.penup()
turtle.home()
turtle.pendown()

rotations = [0, 90, 180, 270]
turtle.pensize(10)
angle = turtle.heading()
for _ in range(100):
    turtle.color(random_color())
    while angle == turtle.heading():
        angle = choice(rotations)
    turtle.setheading(angle)
    turtle.forward(50 * scale)

turtle.penup()
turtle.home()
turtle.pendown()

turtle.pensize(1)
radius = 150
size = 7
for _ in range(int(360 / size)):
    turtle.color(random_color())
    turtle.setheading(turtle.heading() + size)
    turtle.circle(radius)


screen = Screen()
screen.exitonclick()
