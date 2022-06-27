def is_prime(number):
    for i in range(2, number+1):
        if number % i == 0:
            if i == number:
                return True
            else:
                return False
        

def prime_list(number):
    primes = []
    for x in range(2, number):
        if x == 2:
            primes.append(x)
        elif is_prime(x):
            primes.append(x)
    return primes

numbers = int(input("Up to which number do you want all prime numbers: "))

print(prime_list(numbers))
