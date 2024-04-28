#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

from art import logo

DEFAULT_DIFFICULTY = 5

DIFFICULTY_ATTEMPTS = {
    "easy": 10,
    "hard": 5,
}


def check_attempts(attempts, number):
    if attempts > 0:
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts <= 0:
        print("You've run out of guesses, you lose.")
        print(f"The number was {number}")


def choose_difficulty():
    difficulty = input(f"Choose a difficulty, {DIFFICULTY_ATTEMPTS.keys()}: ")
    attempts = DEFAULT_DIFFICULTY
    if difficulty in DIFFICULTY_ATTEMPTS:
        attempts = DIFFICULTY_ATTEMPTS[difficulty]
    return attempts


def play_game():
    print(logo)
    attempts_count = 0
    attempts = choose_difficulty()

    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts > 0:
        attempts_count += 1
        attempts -= 1
        guess = int(input("Make a number guess: "))
        if guess > number:
            print("High.")
            check_attempts(attempts, number)
        elif guess < number:
            print("Low.")
            check_attempts(attempts, number)
        else:
            print(
                f"You got it in {attempts_count} attempts! The answer is {number}."
            )
            break


def game_loop():
    while True:
        play_game()
        if input("Play again? 'y' or 'n': ") != 'y':
            break


game_loop()