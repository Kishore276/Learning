# Factorial Calculator

def factorial_iterative(n):
    """Calculate factorial using iteration"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Calculate factorial using recursion"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

import math
def factorial_builtin(n):
    """Calculate factorial using built-in function"""
    if n < 0:
        return None
    return math.factorial(n)

# Input number
number = int(input("Enter a number to find its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"\nFactorial of {number}:")
    print(f"Using iteration: {factorial_iterative(number)}")
    print(f"Using recursion: {factorial_recursive(number)}")
    print(f"Using built-in function: {factorial_builtin(number)}")
    
    # Show the calculation
    if number <= 10:  # Only show for small numbers
        calculation = " × ".join([str(i) for i in range(1, number + 1)]) if number > 0 else "1"
        print(f"Calculation: {calculation} = {factorial_iterative(number)}")