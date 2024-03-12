import random
import hangman_art
from hangman_words import word_list

print(hangman_art.logo)

stages = hangman_art.stages

end = len(stages) - 1
hidden_symbol = '_';
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = [hidden_symbol] * word_length

guessed = []
mistakes = 0
while mistakes < end and hidden_symbol in display:
  print(display)
  print(stages[mistakes])

  guess = input("Guess a letter: ").lower()
  #from replit import clear
  #clear()

  if guess in guessed:
    print(f"You already attempted the letter '{guess}'")
    print(f"Attempted letters: {guessed}")
    continue

  guessed += guess

  found = False
  for index in range(word_length):
    if chosen_word[index] == guess:
      display[index] = chosen_word[index]
      found = True
    
  if not found:
    print(f"Letter '{guess}' not found")
    mistakes += 1

if mistakes < end:
  print("You win!")
  print(f"Mistake count: {mistakes}")
else:
  print("You lose!")
  print(f'The word was {chosen_word}')