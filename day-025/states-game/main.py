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

guesses = set()
total = len(data)
# print(data[data.state == "Ohio"].iloc[0].x)
# print(type(data))
while len(guesses) < 50:
    guessed = len(guesses)
    guess = screen.textinput(title=f"States Guessed: {guessed}/{total}",
                             prompt="What's another state's name?")
    if guess == "exit":
        break
    guess_data = data[data.state == guess.title()]
    # print(type(guess_data))
    if not guess_data.empty:
        # state = guess_data.state.item()
        first = guess_data.iloc[0]
        state = first.state
        x = first.x
        y = first.y
        pointer.goto(x, y)
        pointer.dot()
        pointer.write(state, font=FONT)
        guesses.add(state)


missed_data = data[~data.state.isin(guesses)]
missing_states = missed_data.state.to_list()
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states-to-learn.csv")

# turtle.mainloop()
# screen.exitonclick()
