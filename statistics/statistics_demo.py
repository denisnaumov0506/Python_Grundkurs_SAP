import random
import statistics

def gaussian_distribution():
    return [random.gauss(100, 10) for x in range(1001)]
    
list_ = gaussian_distribution()
print('Mean: ', statistics.mean(list_))
print('Standard Deviation: ', statistics.stdev(list_))
