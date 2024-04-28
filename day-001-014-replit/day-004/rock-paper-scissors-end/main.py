import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_choice_int = int(user_choice) if (user_choice.isdigit() and int(user_choice) in [0, 1, 2]) else None
if user_choice_int is None: 
  print("You typed an invalid number, you lose!") 
else:
  print(game_images[user_choice_int])
  
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])
  
  if user_choice_int == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice_int == 2:
    print("You lose")
  elif computer_choice > user_choice_int:
    print("You lose")
  elif user_choice_int > computer_choice:
    print("You win!")
  elif computer_choice == user_choice_int:
    print("It's a draw")