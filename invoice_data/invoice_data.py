filename = "invoice_data.txt"

items = []

with open(filename, 'r') as f:
    for line in f:
        item = line.split()
        item_tuple = (item[0], int(item[1]), float(item[2].strip()))
        items.append(item_tuple)

for item in items:
    string = f"{item[0]:<15}{item[1]:>3}{item[2]:>7.2f}{item[1]*item[2]:>8.2f}"
    print(string)

