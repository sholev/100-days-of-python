print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
min_height = 120
bill = 0
if height >= min_height:
  print("You can ride the rollercoaster!")

  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print(f"Child tickets are ${bill}.")
  elif age <= 18:
    bill = 7
    print(f"Youth tickets are ${bill}.")
  elif age >= 45 and age <= 55:
    bill = 0
    print("Everything is going to be ok. Have a free ticket on us!")
  else:
    bill = 12
    print(f"Adult tickets are ${bill}.")

  photo = input("Do you want a photo taken for $3? Y or N. ")
  if photo == "Y":
    bill += 3

  print(f"The total bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")