import random

#from replit import clear

from art import logo, vs

from game_data import data

COUNT_KEY = 'follower_count'


def format_data(info):
  return f"{info['name']}, a {info['description']}, from {info['country']}"


def get_random_data(prefix):
  random_entry = random.choice(data)
  print(f"{prefix}: {format_data(random_entry)}")
  return random_entry


def play_game():
  score = 0
  print(logo)
  a_data = get_random_data("Compare A")
  while True:
    print(vs)
    b_data = get_random_data("Against B")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if (choice == 'a' and a_data[COUNT_KEY] >= b_data[COUNT_KEY]) or (
        choice == 'b' and b_data[COUNT_KEY] >= a_data[COUNT_KEY]):
      a_data = b_data
      #clear()
      print(logo)
      score += 1
      print(f"Correct! Your score is {score}")
      print(f"Compare A: {format_data(a_data)}")
    else:
      print(f"Wrong! Your final score is {score}")
      break


play_game()
