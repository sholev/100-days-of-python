import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter.lower(): row.code for (index, row) in data.iterrows()}


def generate():
    try:
        word = input("Enter a word:").lower()
        result = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print(f"Word contains incorrect letters, use: {alphabet_dict.keys()}")
        generate()
    else:
        print(result)


generate()
