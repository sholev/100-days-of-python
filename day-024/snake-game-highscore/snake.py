from turtle import Turtle

START_POS = ((0, 0), (-20, 0), (-40, 0))
COLOR = "white"
SHAPE = "square"
SEGMENT_SIZE = 20

DIRECTION_UP = 90
DIRECTION_DOWN = 270
DIRECTION_RIGHT = 0
DIRECTION_LEFT = 180


class Snake:

    def __init__(self, color=COLOR, shape=SHAPE,
                 start_pos=START_POS):
        self.segments = []
        self.start_pos = start_pos
        for pos in start_pos:
            self.add_segment(pos, color, shape)
        self.head = self.segments[0]
        self.direction = DIRECTION_RIGHT

    def move(self, distance=SEGMENT_SIZE):
        for index in range(len(self.segments) - 1, 0, -1):
            prev_pos = self.segments[index - 1].position()
            self.segments[index].goto(prev_pos[0], prev_pos[1])

        if self.head.heading() != self.direction:
            if abs(self.head.heading() - self.direction) != 180:
                self.head.setheading(self.direction)

        self.head.forward(distance)

    def add_segment(self, pos, color=COLOR, shape=SHAPE):
        box = Turtle(shape)
        box.penup()
        box.color(color)
        box.goto(pos)
        self.segments.append(box)

    def reset(self):
        while len(self.segments) > len(self.start_pos):
            self.segments[-1].reset()
            self.segments[-1].hideturtle()  # TODO: Pooling maybe?
            del self.segments[-1]
        for (segment, pos) in zip(self.segments, self.start_pos):
            segment.goto(pos)
        self.direction = DIRECTION_RIGHT
        self.head.setheading(DIRECTION_RIGHT)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        self.direction = DIRECTION_UP

    def down(self):
        self.direction = DIRECTION_DOWN

    def right(self):
        self.direction = DIRECTION_RIGHT

    def left(self):
        self.direction = DIRECTION_LEFT
