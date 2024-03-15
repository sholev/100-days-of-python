FILE = "./file.txt"
NEW_FILE = "./new_file.txt"
DESKTOP_FILE_ABS = "/Users/worker/Desktop/drums.json"
DESKTOP_FILE_REL = "../../../../Users/worker/Desktop/drums.json"

with open(FILE) as file:
    contents = file.read()
    print(contents)

with open(FILE, mode="w") as file:
    file.write("Rewrite")

with open(FILE) as file:
    contents = file.read()
    print(contents)

with open(FILE, mode="a") as file:
    file.write("\nAppend")

with open(FILE) as file:
    contents = file.read()
    print(contents)

with open(NEW_FILE, mode="w") as file:
    file.write("Rewrite")

with open(DESKTOP_FILE_ABS) as file:
    contents = file.read()
    print(contents)

with open(DESKTOP_FILE_REL) as file:
    contents = file.read()
    print(contents)