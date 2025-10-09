# All Basic Python Programs - Compact Version

# 1. Check Prime Number or Not & Print First 10 Prime Numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Check prime number
n = 29
print(n, "is Prime?", is_prime(n))

# First 10 prime numbers
count, num, primes = 0, 2, []
while count < 10:
    if is_prime(num):
        primes.append(num)
        count += 1
    num += 1
print("First 10 primes:", primes)

print("\n" + "="*50 + "\n")

# 2. Check Palindrome or Not
s = "madam"
rev = s[::-1]
if s == rev:
    print(s, "is Palindrome")
else:
    print(s, "is Not Palindrome")

print("\n" + "="*50 + "\n")

# 3. Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

print("Fibonacci series (10 terms):")
fibonacci(10)
print()

print("\n" + "="*50 + "\n")

# 4. Swapping Two Numbers
a, b = 5, 10
print("Before Swap: a =", a, "b =", b)
a, b = b, a
print("After Swap: a =", a, "b =", b)

print("\n" + "="*50 + "\n")

# 5. Sort an Array (Without sort method)
arr = [5, 3, 8, 1, 2]
print("Original array:", arr)
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("Sorted array:", arr)

print("\n" + "="*50 + "\n")

# 6. Square Root
import math
n = 16
print("Square root of", n, "=", math.sqrt(n))

print("\n" + "="*50 + "\n")

# 7. Factorial of a Number & Largest/Smallest in Array
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print("Factorial of 5 =", factorial(5))

arr = [10, 4, 8, 20, 2]
print("Array:", arr)
print("Largest:", max(arr))
print("Smallest:", min(arr))

print("\n" + "="*50 + "\n")

# 8. Reverse an Array
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
print("Reversed array:", arr[::-1])

print("\n" + "="*50 + "\n")

# 9. Reverse a String
s = "Python"
print("Original string:", s)
print("Reversed string:", s[::-1])

print("\n" + "="*50 + "\n")

# 10. Find the Sum of Integers of Array
arr = [1, 2, 3, 4, 5]
print("Array:", arr)
print("Sum of elements:", sum(arr))

print("\n" + "="*50 + "\n")

# 11. Leap Year Check
year = 2024
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

print("\n" + "="*50 + "\n")

# 12. Fibonacci Series (Alternative Implementation)
print("Fibonacci series (10 terms) - Alternative:")
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()