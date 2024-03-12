from turtle import Turtle, Screen

speed = 10
angle = 10


def get_turtle():
    t = Turtle()
    t.pensize(5)
    return t


turtle = get_turtle()


def move_forwards():
    print("test")
    turtle.forward(speed)


def move_backwards():
    turtle.backward(speed)


def turn_right():
    turtle.right(angle)


def turn_left():
    turtle.left(angle)


def new_screen():
    screen.clear()
    screen.listen()


def attach_listeners():
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(fun=move_backwards, key="s")
    screen.onkey(turn_right, "d")
    screen.onkey(turn_left, "a")
    screen.onkey(clear, "c")


def clear():
    global turtle
    new_screen()
    turtle = get_turtle()
    attach_listeners()


screen = Screen()
screen.listen()
attach_listeners()


screen.exitonclick()
