def is_prime(number):
    for i in range(2, number+1):
        print(f"number: {number} i: {i} -> {number % i == 0}")
        if number % i == 0:
            if i == number:
                print("Prime! Only divisable by 1 and itself!")
                return True
            else:
                print(f"Not Prime! Not only divasable by 1 and itself! Also divisable by {i}!")
                return False
        

def prime_list(number):
    primes = []
    for x in range(2, number):
        if x == 2:
            primes.append(x)
        elif is_prime(x):
            print()
            primes.append(x)
        else:
            print()
    return primes

numbers = int(input("Up to which number do you want all prime numbers: "))

print(prime_list(numbers))
