from random import choice

choices = ['R', 'P', 'S']

# Generate data
with open("player1.txt", 'w') as f:
    for x in range(0, 100):
        f.write(choice(choices) + "\n")

with open("player2.txt", 'w') as f:
    for x in range(0, 100):
        f.write(choice(choices) + "\n")
