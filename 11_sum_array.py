# Sum of Array Elements

def sum_using_loop(arr):
    """Calculate sum using loop"""
    total = 0
    for element in arr:
        total += element
    return total

def sum_using_builtin(arr):
    """Calculate sum using built-in function"""
    return sum(arr)

def sum_using_recursion(arr, index=0):
    """Calculate sum using recursion"""
    if index >= len(arr):
        return 0
    return arr[index] + sum_using_recursion(arr, index + 1)

def sum_using_reduce(arr):
    """Calculate sum using reduce function"""
    from functools import reduce
    return reduce(lambda x, y: x + y, arr, 0)

def calculate_statistics(arr):
    """Calculate various statistics"""
    if not arr:
        return None
    
    total = sum(arr)
    count = len(arr)
    average = total / count
    
    return {
        'sum': total,
        'count': count,
        'average': average,
        'min': min(arr),
        'max': max(arr)
    }

# Input array
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print(f"Array: {arr}")

# Calculate sum using different methods
sum1 = sum_using_loop(arr)
sum2 = sum_using_builtin(arr)
sum3 = sum_using_recursion(arr)
sum4 = sum_using_reduce(arr)

print(f"\nSum calculations:")
print(f"Using loop: {sum1}")
print(f"Using built-in: {sum2}")
print(f"Using recursion: {sum3}")
print(f"Using reduce: {sum4}")

# Calculate statistics
stats = calculate_statistics(arr)
print(f"\nArray statistics:")
for key, value in stats.items():
    print(f"{key.capitalize()}: {value}")