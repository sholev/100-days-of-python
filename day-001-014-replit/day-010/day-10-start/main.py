
def format_name(f_name, l_name):
  """Take first and last name and format them to Tittle case"""

  if f_name == "" or l_name == "":
    return "Invalid input"

  return f"{f_name.title()} {l_name.title()}"
  
print(format_name("james", "smith"))
print(format_name("", "smith"))