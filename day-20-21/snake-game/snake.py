from turtle import Turtle

SNAKE_START_POS = ((0, 0), (-20, 0), (-40, 0))
SNAKE_COLOR = "white"
SNAKE_SHAPE = "square"
SNAKE_SEGMENT_SIZE = 20

DIRECTION_UP = 90
DIRECTION_DOWN = 270
DIRECTION_RIGHT = 0
DIRECTION_LEFT = 180


class Snake:

    def __init__(self, color=SNAKE_COLOR, shape=SNAKE_SHAPE,
                 start_pos=SNAKE_START_POS):
        self.segments = []
        for pos in start_pos:
            box = Turtle(shape)
            box.penup()
            box.color(color)
            box.goto(pos)
            self.segments.append(box)
        self.head = self.segments[0]
        self.direction = DIRECTION_RIGHT

    def move(self, distance=SNAKE_SEGMENT_SIZE):
        for index in range(len(self.segments) - 1, 0, -1):
            prev_pos = self.segments[index - 1].position()
            self.segments[index].goto(prev_pos[0], prev_pos[1])

        if self.head.heading() != self.direction:
            if abs(self.head.heading() - self.direction) != 180:
                self.head.setheading(self.direction)

        self.head.forward(distance)

    def up(self):
        self.direction = DIRECTION_UP

    def down(self):
        self.direction = DIRECTION_DOWN

    def right(self):
        self.direction = DIRECTION_RIGHT

    def left(self):
        self.direction = DIRECTION_LEFT
