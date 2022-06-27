from random import sample
from random import choice

global list_of_letters
list_of_letters = []

def word_list():
    list_of_words = []
    with open('5_letter_words.txt', 'r') as file:
        for line in file:
            list_of_words.append(line.strip())
    return list_of_words

def random_word(list_of_words):
    return sample(list_of_words, k=1)[0]

def is_real_word(guess, list_of_words):
    return guess in list_of_words

def check_guess(guess, target):
    string = ''
    double_words = []

    for letter_guess, letter_target in zip(guess, target):

        if letter_guess == letter_target and\
            letter_guess not in double_words:
            string += 'X'
            update_list_of_letters(letter_guess)
        elif letter_guess in target and\
            letter_guess not in double_words:
            string += 'O'
            update_list_of_letters(letter_guess)
        elif letter_guess not in target or\
            letter_guess in double_words:
            string += '_'

        if guess.count(letter_guess) > target.count(letter_guess):
            if letter_guess not in double_words:
                double_words.append(letter_guess)
    return list_of_letters, string

def next_guess(list_of_words):
    while True:
        guess = input('Please enter a guess: ').lower()

        if is_real_word(guess, list_of_words):
            return guess
        print("That's not a real word!")
        continue

def update_list_of_letters(letter):
    list_of_letters.append(letter)

def is_letter_in_word(list_of_letters, list_of_words):
    new_list = list_of_words[:]

    for word in list_of_words:
        for letter in list_of_letters:
            if letter not in word and word in new_list:
                new_list.remove(word)

    return new_list
    

def play():
    list_of_words = word_list()
    random_choice = random_word(list_of_words)
    #print(f'Random_choice is: {random_choice}')
    list_of_letters = []
    for x in range(6):
        guess = next_guess(list_of_words)
        list_, result = check_guess(guess, random_choice)
        list_of_letters = list(set(list_of_letters + list_))
        print("You have guessed these letters correctly: ", list_of_letters)
        print(result)
        print("Your word is among these words: ", is_letter_in_word(list_of_letters, list_of_words), sep='\n')
        if result == 'XXXXX':
            print('You won!')
            break
        if x == 5:
            print('You lost!')
            print(f"The word was: {random_choice}")

play()