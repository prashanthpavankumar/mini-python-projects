import math

def prime(n):
    if n <= 1:
        print(f"{n} is not a prime number")
        return
    
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
    
    if not factors:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number and the factors are {factors}")

a = int(input("Enter a number: "))
prime(a)
