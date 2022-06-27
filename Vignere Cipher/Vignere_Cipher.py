alphabet = {}
for i in range(26):
    alphabet[chr(97+i)] = i

print(alphabet)

def encrypt_letter(char, key):
    if char.isalpha():
        num = calculate_shifts(key) + calculate_shifts(char)
        return chr(num%26+97)
    return char

def calculate_shifts(letter):
    if letter not in alphabet:
        return letter
    return alphabet[letter]

def encrypt_text(msg, key):
    string = ""
    for x in range(len(msg)):
        string += encrypt_letter(msg.lower()[x], key.lower()[x % len(key.lower())])
    return string

message = input("Please enter a message: ")
keyword = input("Which keyword should be used: ")

print(encrypt_text(message, keyword))

