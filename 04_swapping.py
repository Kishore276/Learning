# Swapping Two Numbers - Different Methods

def swap_with_temp(a, b):
    """Swap using temporary variable"""
    temp = a
    a = b
    b = temp
    return a, b

def swap_without_temp(a, b):
    """Swap without temporary variable using arithmetic"""
    a = a + b
    b = a - b
    a = a - b
    return a, b

def swap_with_xor(a, b):
    """Swap using XOR operation (works only with integers)"""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

def swap_pythonic(a, b):
    """Pythonic way of swapping"""
    a, b = b, a
    return a, b

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Original values: a = {num1}, b = {num2}")

# Method 1: Using temporary variable
a1, b1 = swap_with_temp(num1, num2)
print(f"After swapping (with temp): a = {a1}, b = {b1}")

# Method 2: Without temporary variable
a2, b2 = swap_without_temp(num1, num2)
print(f"After swapping (without temp): a = {a2}, b = {b2}")

# Method 3: XOR (only for integers)
if num1.is_integer() and num2.is_integer():
    a3, b3 = swap_with_xor(int(num1), int(num2))
    print(f"After swapping (XOR): a = {a3}, b = {b3}")

# Method 4: Pythonic way
a4, b4 = swap_pythonic(num1, num2)
print(f"After swapping (Pythonic): a = {a4}, b = {b4}")