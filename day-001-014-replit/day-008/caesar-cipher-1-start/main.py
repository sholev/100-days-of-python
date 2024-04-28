alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

alphabet_length = len(alphabet)


def ceaser(text, shift, direction):
    shift = shift % alphabet_length
    if direction == "decode":
        shift *= -1

    result = ""
    for letter in text:
        try:
            index = alphabet.index(letter)
            new_index = (index + shift) % alphabet_length
            result += alphabet[new_index]
        except:
            result += letter

    return result


while True:
    action = input("Type 'encode', 'decode' or 'exit':\n")
    if action == "exit":
        break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(ceaser(text, shift, action))
