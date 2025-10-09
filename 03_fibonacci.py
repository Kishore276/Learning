# Fibonacci Number and Series

def fibonacci_number(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_series(n):
    """Generate Fibonacci series up to n terms"""
    series = []
    a, b = 0, 1
    for i in range(n):
        if i == 0:
            series.append(a)
        elif i == 1:
            series.append(b)
        else:
            next_fib = a + b
            series.append(next_fib)
            a, b = b, next_fib
    return series

# Calculate nth Fibonacci number
n = int(input("Enter the position to find Fibonacci number: "))
fib_num = fibonacci_number(n)
print(f"The {n}th Fibonacci number is: {fib_num}")

# Generate Fibonacci series
terms = int(input("Enter number of terms for Fibonacci series: "))
fib_series = fibonacci_series(terms)
print(f"Fibonacci series of {terms} terms:")
print(fib_series)