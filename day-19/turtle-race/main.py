import random
from turtle import Turtle, Screen
from tkinter import messagebox


width = 500
height = 400
start_pos = -230
finish_pos = 230
y_offset = -30

screen = Screen()
screen.setup(width=width, height=height)
user_bet = screen.textinput(title="Make your bet", prompt="Winner color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def initialize_turtles(input_colors):
    new_turtles = []
    index = 1
    for color in input_colors:
        x = start_pos
        y = (height / 2 * -1) + (height / len(input_colors)) * index + y_offset
        index += 1

        new_turtle = Turtle("turtle")
        new_turtle.color(color)
        new_turtle.speed("fast")
        new_turtle.penup()
        new_turtle.goto(x, y)
        new_turtles.append(new_turtle)
    return new_turtles


def show_win_message():
    winner = max(turtles, key=lambda t: t.position()[0]).pencolor()
    title = f"You {"win" if winner == user_bet else "lose"}!"
    message = f"Winner is {winner}"
    messagebox.showinfo(title, message)


if user_bet in colors:
    turtles = initialize_turtles(colors)
    while True:
        for turtle in turtles:
            random_speed = random.randint(0, 10)
            turtle.forward(random_speed)

        if any(turtle.position()[0] >= finish_pos for turtle in turtles):
            show_win_message()
            break


screen.exitonclick()
