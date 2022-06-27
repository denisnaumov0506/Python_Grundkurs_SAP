filename = "numbers.txt"
with open(filename) as f:
    numbers = f.readlines()
test = []
for x in numbers:
    number = int(x.strip())
    test.append(number)
for x in range(0, 3):
    largest = max(test)
    test.remove(max(test))
    print(largest)
