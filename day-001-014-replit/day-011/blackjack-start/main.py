import random

from art import logo

from replit import clear

available_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_ace = 11

dealer_draw = 17
player_draw = 21

option_hit = "hit"
option_stand = "stand"


def format_cards(n, cards):
  result = ""
  for i in range(n):
    result += "" if i == 0 else ", "
    result += str(cards[i])
  return result


def add_random_cards(n, list):
  for i in range(n):
    list.append(random.choice(available_cards))


def get_score(cards):
  score = sum(cards)
  while score > player_draw and card_ace in cards:
    cards[cards.index(card_ace)] = 1
    score = sum(cards)
  return score


def create_start_cards(prefix, num_visible, num_cards, cards):
  add_random_cards(num_cards, cards)
  print(f"{prefix}: {format_cards(num_visible, cards)}")
  return get_score(cards)
  

def print_result(prefix, num_visible, cards, score):
  print(f"{prefix}: {format_cards(num_visible, cards)}, score: {score}")


def play_game():
  dealer_cards = []
  player_cards = []

  dealer_score = create_start_cards("Dealer's card", 1, 2, dealer_cards)
  player_score = create_start_cards("Player's cards", 2, 2, player_cards)

  choice = input(f"{option_hit}/{option_stand}: ")
  while choice == option_hit and player_score < player_draw:
    add_random_cards(1, player_cards)
    player_score = get_score(player_cards)
    print(f"Player's cards: {format_cards(len(player_cards), player_cards)}")
    if (player_score > player_draw):
      break
    choice = input(f"{option_hit}/{option_stand}: ")

  if choice == option_stand:
    while dealer_score < dealer_draw:
      add_random_cards(1, dealer_cards)
      dealer_score = get_score(dealer_cards)

  print_result("Dealer's result", len(dealer_cards), dealer_cards,
               dealer_score)
  print_result("Player's result", len(player_cards), player_cards,
               player_score)

  if player_score > player_draw:
    print("Bust! You lose.")
  elif dealer_score > player_draw:
    print("Dealer bust! You win.")
  elif player_score == dealer_score:
    print(f"Draw! {player_score} vs {dealer_score}")
  elif player_score > dealer_score:
    print(f"You win! {player_score} vs {dealer_score}")
  else:
    print(f"You lose! {player_score} vs {dealer_score}")


while True:
  clear()
  print(logo)
  play_game()
  if input("Play again? (y/n):") != "y":
    break

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
