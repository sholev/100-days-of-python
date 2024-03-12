################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

#Avoid:
def increase_enemies_global_scope():
  global enemies
  enemies = 3
  print(f"enemies inside global scope function: {enemies}")

def increase_enemies_return(n):
  return enemies + n

increase_enemies()
print(f"enemies outside function: {enemies}")
increase_enemies_global_scope()
print(f"enemies outside function: {enemies}")
enemies = increase_enemies_return(1)
print(f"enemies outside function: {enemies}")


# No block scope:

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy)

#Global constants:
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

