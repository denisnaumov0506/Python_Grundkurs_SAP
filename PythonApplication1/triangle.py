while True:
    degrees = []

    for x in range(3):
        degree = int(input(f"Please enter the value of the degree number {x+1}: "))
        if (degree<=0 or degree >= 180):
            print("Invalid degree was submitted! Please try again!")
            break
        degrees.append(degree)

    if len(degrees)!=3:
        continue
    
    if sum(degrees) > 180:
        print("The sum of the degrees is too high! Please enter valid options!")
        continue
    else:
        string = "We have identified your triangle as "
        if degrees.count(90)==1:
            string += "a right angle triangle"
        elif len([x for x in degrees if x > 90])==1:
            string += "an obtuse triangle"
        else:
            string += "an acute triangle"
        print(string)

    break

