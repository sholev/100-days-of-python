# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(name):
  print(f"Hello there {str(name)}")

def greet_with(name, location):
  print(f"Hello there {str(name)}")
  print(f"It's a fine day at {str(location)}, isn't it?")

greet_with("Sen", "Asgard")
greet_with(location="Asgard", name=None)