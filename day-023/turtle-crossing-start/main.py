import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

UPDATE = 0.01
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player(speed=3)
scoreboard = Scoreboard(pos=(-200, 250))
car_manager = CarManager(update_interval=10, starting_move_distance=3)
for _ in range(100):
    car_manager.update()

screen.update()
screen.listen()
screen.onkeypress(player.move, "w")
screen.onkeyrelease(player.stay, "w")
screen.onkeypress(player.move, "Up")
screen.onkeyrelease(player.stay, "Up")

game_is_on = True
while game_is_on:
    time.sleep(UPDATE)
    screen.update()
    player.update()
    car_manager.update()

    if car_manager.get_collision(player) is not None:
        scoreboard.write_game_over()
        game_is_on = False

    if player.is_finished():
        player.restart()
        car_manager.increase_speed(increase=1)
        scoreboard.increment()


screen.exitonclick()
