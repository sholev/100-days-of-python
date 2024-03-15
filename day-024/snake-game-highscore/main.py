import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
WALL = 281
TITLE = "Snake Game"
COLOR = 'black'
UPDATE = 0.1
COLLISION = 19

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(COLOR)
screen.title(TITLE)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.onkey(snake.up, "W")
screen.onkey(snake.down, "S")
screen.onkey(snake.left, "A")
screen.onkey(snake.right, "D")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(UPDATE)
    snake.move()

    if snake.head.distance(food) < COLLISION:
        food.refresh()
        scoreboard.increment()
        snake.grow()

    if abs(snake.head.xcor()) > WALL or abs(snake.head.ycor()) > WALL:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < COLLISION:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
