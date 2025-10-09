# Square Root Calculator

import math

def sqrt_using_builtin(n):
    """Calculate square root using built-in function"""
    return math.sqrt(n)

def sqrt_using_power(n):
    """Calculate square root using power operator"""
    return n ** 0.5

def sqrt_babylonian_method(n, precision=1e-10):
    """Calculate square root using Babylonian method (Newton's method)"""
    if n < 0:
        return None
    if n == 0:
        return 0
    
    guess = n / 2.0
    while abs(guess * guess - n) > precision:
        guess = (guess + n / guess) / 2.0
    return guess

def sqrt_binary_search(n, precision=1e-10):
    """Calculate square root using binary search"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return n
    
    start = 0
    end = n if n > 1 else 1
    
    while end - start > precision:
        mid = (start + end) / 2.0
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            start = mid
        else:
            end = mid
    
    return (start + end) / 2.0

# Input number
number = float(input("Enter a number to find its square root: "))

if number < 0:
    print("Square root of negative number is not real")
else:
    print(f"\nSquare root of {number}:")
    print(f"Using built-in function: {sqrt_using_builtin(number)}")
    print(f"Using power operator: {sqrt_using_power(number)}")
    print(f"Using Babylonian method: {sqrt_babylonian_method(number)}")
    print(f"Using binary search: {sqrt_binary_search(number)}")