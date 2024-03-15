STARTING_LETTER = "./Input/Letters/starting_letter.txt"
NAMES = "./Input/Names/invited_names.txt"
READY_FOLDER = "./Output/ReadyToSend/"
LETTER_FILE_NAME = "letter_for_{0}.txt"


with open(STARTING_LETTER) as letter, open(NAMES) as names:
    letter_text = letter.read()
    for line in names.readlines():
        line = line.strip()
        replaced_letter = letter_text.replace("[name]", line)
        new_file_name = READY_FOLDER + LETTER_FILE_NAME.format(line)
        print(f"Saving file: {new_file_name}")
        with open(new_file_name, mode="w") as new_letter:
            new_letter.write(replaced_letter)

