# Reverse an Array

def reverse_array_inplace(arr):
    """Reverse array in-place using two pointers"""
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

def reverse_array_slicing(arr):
    """Reverse array using slicing"""
    return arr[::-1]

def reverse_array_builtin(arr):
    """Reverse array using built-in reverse function"""
    arr_copy = arr.copy()
    arr_copy.reverse()
    return arr_copy

def reverse_array_loop(arr):
    """Reverse array using loop"""
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Input array
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print(f"Original array: {arr}")

# Reverse using different methods
reversed1 = reverse_array_inplace(arr.copy())
reversed2 = reverse_array_slicing(arr)
reversed3 = reverse_array_builtin(arr)
reversed4 = reverse_array_loop(arr)

print(f"Reversed (in-place): {reversed1}")
print(f"Reversed (slicing): {reversed2}")
print(f"Reversed (built-in): {reversed3}")
print(f"Reversed (loop): {reversed4}")