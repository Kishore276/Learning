# Largest and Smallest Element in Array

def find_largest_smallest(arr):
    """Find largest and smallest elements in array"""
    if not arr:
        return None, None
    
    largest = smallest = arr[0]
    
    for element in arr[1:]:
        if element > largest:
            largest = element
        if element < smallest:
            smallest = element
    
    return largest, smallest

def find_using_builtin(arr):
    """Find largest and smallest using built-in functions"""
    if not arr:
        return None, None
    return max(arr), min(arr)

def find_with_sorting(arr):
    """Find largest and smallest by sorting"""
    if not arr:
        return None, None
    
    sorted_arr = sorted(arr)
    return sorted_arr[-1], sorted_arr[0]

# Input array
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print(f"Array: {arr}")

# Find largest and smallest using different methods
largest1, smallest1 = find_largest_smallest(arr)
largest2, smallest2 = find_using_builtin(arr)
largest3, smallest3 = find_with_sorting(arr)

print(f"\nUsing linear search:")
print(f"Largest element: {largest1}")
print(f"Smallest element: {smallest1}")

print(f"\nUsing built-in functions:")
print(f"Largest element: {largest2}")
print(f"Smallest element: {smallest2}")

print(f"\nUsing sorting:")
print(f"Largest element: {largest3}")
print(f"Smallest element: {smallest3}")