import turtle, random

import colorgram


def extract_colors():
    colorgram_colors = colorgram.extract('image.webp', 30)
    white_filter = 230
    rgb_colors = []
    for color in colorgram_colors:
        color = (color.rgb.r, color.rgb.g, color.rgb.b)
        if color[0] > white_filter and color[1] > white_filter and color[
            2] > white_filter:
            continue
        rgb_colors.append(color)
    return rgb_colors


# print(extract_colors())

colors = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160),
          (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32),
          (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19),
          (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162),
          (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85),
          (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216),
          (253, 197, 0), (80, 135, 179)]


def turtle_grid(width, height, scale):
    turtle.colormode(255)
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.speed(100)
    start_pos_x = t.position()[0] - (width / 2) + 0.5
    start_pos_y = t.position()[1] - (height / 2) + 0.5
    for y in range(height):
        for x in range(width):
            target_x = (start_pos_x + x) * 100 * scale
            target_y = (start_pos_y + y) * 100 * scale
            t.goto(target_x, target_y)
            t.color(random.choice(colors))
            t.pendown()
            t.dot(50 * scale)
            t.penup()


turtle_grid(12, 10, 1)

s = turtle.Screen()
s.exitonclick()
