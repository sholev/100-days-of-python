import pandas
import turtle

FONT = ("Arial", 21, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pointer = turtle.Turtle("circle")
pointer.shapesize(0.5, 0.5)
pointer.penup()

data = pandas.read_csv("50_states.csv")

guessed = set()
total = len(data)

while len(guessed) < 50:
    guess = screen.textinput(title=f"States Guessed: {len(guessed)}/{total}",
                             prompt="What's another state's name?")
    if guess == "exit":
        missing_states = [s for s in data.state.to_list() if s not in guessed]
        new_data = pandas.DataFrame(missing_states)
        print(new_data)
        # new_data.to_csv("states-to-learn.csv")
        break

    guess_data = data[data.state == guess.title()]
    if not guess_data.empty:
        first = guess_data.iloc[0]
        pointer.goto(first.x, first.y)
        pointer.dot()
        pointer.write(first.state, font=FONT)
        guessed.add(first.state)

