from turtle import Turtle

START_POS = (-400, -400)
END_POS = (400, 400)
LENGTH = 200
COLOR = "white"
SHAPE = "square"
SEGMENT_SIZE = 20


def split_vectors(v1, v2, n):
    """Splits the distance between two 2D vectors into N evenly spaced vectors.

    Args:
        v1: First 2D vector (list).
        v2: Second 2D vector (list).
        n: Number of intermediate vectors to generate (including endpoints).

    Returns:
        A list of N 2D vectors representing the evenly spaced points.
    """

    # Calculate the difference in each dimension
    diff_x = (v2[0] - v1[0]) / (n - 1)
    diff_y = (v2[1] - v1[1]) / (n - 1)

    # Generate intermediate vectors
    intermediate_vectors = []
    for i in range(n):
        x = v1[0] + i * diff_x
        y = v1[1] + i * diff_y
        intermediate_vectors.append([x, y])

    return intermediate_vectors


class Wall:

    def __init__(self, color=COLOR, shape=SHAPE, start_pos=START_POS,
                 end_pos=END_POS):
        self.segments = []
        self.add_segment(start_pos)
        self.add_segment(end_pos)
        distance = self.segments[0].distance(end_pos[0], end_pos[1])
        count = int(distance / SEGMENT_SIZE)
        vectors = split_vectors(start_pos, end_pos, count)
        for pos in vectors:
            self.add_segment(pos, color, shape)

    def add_segment(self, pos, color=COLOR, shape=SHAPE):
        box = Turtle(shape)
        box.penup()
        box.color(color)
        box.goto(pos)
        self.segments.append(box)

