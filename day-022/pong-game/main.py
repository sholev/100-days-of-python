import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard

# from scoreboard import Scoreboard

WIDTH = 900
HEIGHT = 600
SIDE_WALL = (WIDTH / 2)
UP_DOWN_WALL = (HEIGHT / 2)
UPDATE = 0.01
PADDLE_X = SIDE_WALL - 40
PADDLE_LEFT_START = ((-PADDLE_X, -20), (-PADDLE_X, 0), (-PADDLE_X, 20))
PADDLE_RIGHT_START = ((PADDLE_X, -20), (PADDLE_X, 0), (PADDLE_X, 20))
PADDLE_SPEED = 10
PADDLE_SIZE = 1

BALL_SPEED = 7
BALL_SPEED_INCREASE = 1

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

wall_up = Wall(start_pos=(SIDE_WALL, UP_DOWN_WALL),
               end_pos=(-SIDE_WALL, UP_DOWN_WALL))
wall_down = Wall(start_pos=(SIDE_WALL, -UP_DOWN_WALL),
                 end_pos=(-SIDE_WALL, -UP_DOWN_WALL))

wall_right = Wall(color="red", start_pos=(SIDE_WALL + 40, UP_DOWN_WALL),
                  end_pos=(SIDE_WALL + 40, -UP_DOWN_WALL))
wall_left = Wall(color="red", start_pos=(-SIDE_WALL - 40, UP_DOWN_WALL),
                 end_pos=(-SIDE_WALL - 40, -UP_DOWN_WALL))

left_paddle = Paddle(start_pos=PADDLE_LEFT_START, move_speed=PADDLE_SPEED,
                     size=PADDLE_SIZE)
right_paddle = Paddle(start_pos=PADDLE_RIGHT_START, move_speed=PADDLE_SPEED,
                      size=PADDLE_SIZE)

ball = Ball(move_speed=BALL_SPEED)
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeyrelease(left_paddle.stay, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeyrelease(left_paddle.stay, "s")

screen.onkeypress(right_paddle.up, "Up")
screen.onkeyrelease(right_paddle.stay, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeyrelease(right_paddle.stay, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(UPDATE)
    ball.move()
    left_paddle.move()
    right_paddle.move()

    walls = wall_up.segments + wall_down.segments
    if ball.check_collision(walls) is not None:
        ball.bounce_y()

    if ball.check_collision(left_paddle.segments) is not None:
        if ball.velocity[0] < 0:
            ball.bounce_x(BALL_SPEED_INCREASE)

    if ball.check_collision(right_paddle.segments) is not None:
        if ball.velocity[0] > 0:
            ball.bounce_x(BALL_SPEED_INCREASE)

    if ball.check_collision(wall_left.segments) is not None:
        scoreboard.r_increment()
        ball.restart(BALL_SPEED)

    if ball.check_collision(wall_right.segments) is not None:
        scoreboard.l_increment()
        ball.restart(BALL_SPEED)

screen.exitonclick()
