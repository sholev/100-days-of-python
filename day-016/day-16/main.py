def test_turtle():
    from turtle import Screen, Turtle
    screen = Screen()
    turtle = Turtle()

    print(turtle)
    print(screen.canvheight)

    turtle.shape("turtle")
    turtle.color("green")
    turtle.forward(100)
    turtle.goto(500, 500)
    screen.exitonclick()


# test_turtle()

def test_pretty_table():
    from prettytable import PrettyTable
    table = PrettyTable()
    table.add_column("Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])
    table.align = "l"
    return table


print(test_pretty_table())