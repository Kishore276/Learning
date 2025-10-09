# Prime Number Checker and First 10 Prime Numbers

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def first_n_primes(n):
    """Generate first n prime numbers"""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Check if a number is prime
number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

# Print first 10 prime numbers
print("\nFirst 10 prime numbers:")
prime_list = first_n_primes(10)
print(prime_list)