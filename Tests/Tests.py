list_ = [1, 1, 2, 2, 3, 3]


# for loop -> schl�gt fehl
for x in list_:
    list_.remove(2)

# while loop -> funktioniert
while 2 in list_:
    list_.remove(2)