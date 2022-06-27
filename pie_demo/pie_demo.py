from random import random as r
import math

x_y = [(r(), r()) for x in range(10000)]
total_num = len(x_y)

points_within_circle = [x for x in x_y if ((x[0]**2)+(x[1]**2)) < 1]
square_numbers = len(points_within_circle)

print('Calculated value of \u03C0: ', 4*(square_numbers/total_num))
print('Value of \u03C0 from math library: ', math.pi)
print('Difference: ', 4*(square_numbers/total_num)-math.pi)

