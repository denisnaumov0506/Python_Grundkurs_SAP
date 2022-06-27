secret = []

with open("secret.txt", 'r') as f:
    for line in f:
        secret.append(line.strip())

with open("key.txt", 'r') as f:
    number_of_cols = int(f.readline().strip())
    number_of_rows = int(f.readline().strip())

secret_message = []

for current_row in range(0, number_of_rows):
    line = ''
    for current_col in range(0, number_of_cols):
        line += secret[current_col+(current_row*number_of_cols)]
    secret_message.append(line)

with open("public.txt", 'w') as f:
    for line in secret_message:
        f.write(line + "\n")