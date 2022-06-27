alphabet = {
    'a': 0, 'b': 1, 'c': 2,
    'd': 3, 'e': 4, 'f': 5,
    'g': 6, 'h': 7, 'i': 8,
    'j': 9, 'k': 10, 'l': 11,
    'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17,
    's': 18, 't': 19, 'u': 20,
    'v': 21, 'w': 22, 'x': 23,
    'y': 24, 'z': 25,
    }


def encrypt_letter(char, key):
    if char.isalpha():
        num = alphabet[char]
        for key in alphabet:
            if alphabet[key] == (key+num) % 26:
                return key
    return char

def calculate_shifts(letter):
    return alphabet[letter]

def encrypt_text(msg, key):
    string = ""
    for x in range(len(msg)):
        my_key = calculate_shifts(key.lower()[x % len(key.lower())])
        string += encrypt_letter(msg.lower()[x], my_key)
    return string

message = input("Please enter a message: ")
keyword = input("Which keyword should be used: ")

print(encrypt_text(message, keyword))
