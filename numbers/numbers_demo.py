filename = "numbers.txt"

with open(filename) as f:
    numbers = []
    while True:
        number = f.readline().strip()
        if number == '':
            f.close() # good practice
            break
        numbers.append(int(number))

for x in range(0, 3):
    largest = max(numbers)
    numbers.remove(max(numbers))
    print(largest)