shift = input('Please enter the number of places to shift: ')
if shift.isdecimal() and int(shift) >= 0 and int(shift) < 26:
    shift = int(shift)
    message = input('Please enter a sentence: ').lower()
    encryption = ''

    for letter in message:
        if ord(letter) > 122-shift and ord(letter) < 123:
            encryption += chr(ord(letter)%(122-shift)+96)
        elif(ord(letter) > 96 and ord(letter) < 123):
            encryption += chr(ord(letter)+shift)
        else:
            encryption += letter

    print(encryption)
else:
    print('You need to enter a number between 0 and 25!')