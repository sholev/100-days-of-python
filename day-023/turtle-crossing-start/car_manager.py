import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
UPDATE = 6
SHAPE = "square"
SIZE = (1, 2)
DIRECTION = 180


class CarManager:

    def __init__(self, update_interval=UPDATE, y_range=(-230, 230), x_pos=300,
                 starting_move_distance=STARTING_MOVE_DISTANCE):
        self.update_interval = update_interval
        self.y_range = y_range
        self.x_pos = x_pos
        self.move_distance = starting_move_distance
        self.update_counter = 0
        self.cars = []

    def add_car(self, pos, shape=SHAPE):
        car = Turtle(shape)
        car.penup()
        car.color(random.choice(COLORS))
        car.setheading(DIRECTION)
        car.turtlesize(SIZE[0], SIZE[1])
        car.goto(pos)
        self.cars.append(car)

    def update(self):
        self.update_counter += 1
        if self.update_counter % self.update_interval == 0:
            y_pos = random.randint(self.y_range[0], self.y_range[1])
            if len(self.cars) <= 0 or self.cars[0].xcor() > -self.x_pos:
                self.add_car((self.x_pos, y_pos))
            else:
                car = self.cars[0]
                car.goto((self.x_pos, y_pos))
                self.cars.remove(car)
                self.cars.append(car)

        for car in self.cars:
            car.forward(self.move_distance)

    def increase_speed(self, increase=MOVE_INCREMENT):
        self.move_distance += increase

    def get_collision(self, other, collision_distance=19):
        for car in self.cars:
            if car.distance(other) <= collision_distance:
                return car
