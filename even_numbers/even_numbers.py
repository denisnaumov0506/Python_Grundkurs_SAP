filename = "numbers.txt"
even_numbers = []

with open(filename, 'r') as f:
    for line in f:
        if int(line.strip()) % 2 == 0:
            even_numbers.append(int(line.strip()))

filename = "even_numbers.txt"

with open(filename, 'w') as f:
    for number in even_numbers:
        f.write(str(number) + '\n')

print("List of even numbers created!")