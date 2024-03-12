#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for n in range(0, nr_letters):
  random_index = random.randint(0, len(letters) - 1)
  password += letters[random_index]
for n in range(0, nr_symbols):
  random_index = random.randint(0, len(symbols) - 1)
  password += symbols[random_index]
for n in range(0, nr_numbers):
  random_index = random.randint(0, len(numbers) - 1)
  password += numbers[random_index]

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for n in range(0, nr_letters):
  random_index = random.randint(0, len(letters) - 1)
  insert_index = random.randint(0, max(0, len(password_list) - 1))
  char = letters[random_index]
  password_list.insert(insert_index, char)
for n in range(0, nr_symbols):
  random_index = random.randint(0, len(symbols) - 1)
  insert_index = random.randint(0, max(0, len(password_list) - 1))
  char = symbols[random_index]
  password_list.insert(insert_index, char)
for n in range(0, nr_numbers):
  random_index = random.randint(0, len(numbers) - 1)
  insert_index = random.randint(0, max(0, len(password_list) - 1))
  char = numbers[random_index]
  password_list.insert(insert_index, char)

print(''.join(password_list))

#Final:
password_list = []
for n in range(0, nr_letters):
  password_list += random.choice(letters)
for n in range(0, nr_symbols):
  password_list += random.choice(symbols)
for n in range(0, nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)
print(''.join(password_list))