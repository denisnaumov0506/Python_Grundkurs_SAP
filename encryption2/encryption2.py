shifted_alphabet = {
    'a': 'f', 'b': 'g',
    'c': 'h', 'd': 'i',
    'e': 'j', 'f': 'k',
    'g': 'l', 'h': 'm',
    'i': 'n', 'j': 'o',
    'k': 'p', 'l': 'q',
    'm': 'r', 'n': 's',
    'o': 't', 'p': 'u',
    'q': 'v', 'r': 'w',
    's': 'x', 't': 'y',
    'u': 'z', 'v': 'a',
    'w': 'b', 'x': 'c',
    'y': 'd', 'z': 'e',
    }

sentence = input('Please enter a sentence: ').lower()
new_sentence = ''

for x in range(len(sentence)):
    print(sentence[x])
    if sentence[x] in shifted_alphabet.keys():
        new_sentence += shifted_alphabet[sentence[x]]
    else:
        new_sentence += sentence[x]

print(new_sentence)
