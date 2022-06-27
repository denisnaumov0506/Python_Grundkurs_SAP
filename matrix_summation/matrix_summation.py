rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

matrix = []

for x in range(rows):
    matrix.append([])

print("Enter the matrix values: ")
for row in range(rows):
    for column in range(columns):
        matrix[row].append(int(input("Value: ")))

for x in range(rows):
    print(f"Sum of row {x+1} is " + str(sum(matrix[x])))

