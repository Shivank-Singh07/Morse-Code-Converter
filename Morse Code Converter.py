morse_code = {
    "A": "•-",
    "B": "-•••",
    "C": "-•-•",
    "D": "-••",
    "E": "•",
    "F": "••-•",
    "G": "--•",
    "H": "••••",
    "I": "••",
    "J": "•---",
    "K": "-•-",
    "L": "•-••",
    "M": "--",
    "N": "-•",
    "O": "---",
    "P": "•--•",
    "Q": "--•-",
    "R": "•-•",
    "S": "•••",
    "T": "-",
    "U": "••-",
    "V": "•••-",
    "W": "•--",
    "X": "-••-",
    "Y": "-•--",
    "Z": "--••",
    "1": "•----",
    "2": "••---",
    "3": "•••--",
    "4": "••••-",
    "5": "•••••",
    "6": "-••••",
    "7": "--•••",
    "8": "---••",
    "9": "----•",
    "0": "-----",
}


def convert(text):
    sliced_text = [c for c in text]
    converted_text = []
    for i in sliced_text:
        try:
            converted_text.append(morse_code[i])
        except KeyError:
            converted_text.append(i)
    print(" ".join(converted_text))


while True:
    text_input = input("Enter the text: ").upper()
    convert(text_input)
