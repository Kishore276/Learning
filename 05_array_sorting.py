# Array Sorting - Different Algorithms

def bubble_sort(arr):
    """Bubble sort implementation"""
    n = len(arr)
    arr_copy = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy

def selection_sort(arr):
    """Selection sort implementation"""
    n = len(arr)
    arr_copy = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    return arr_copy

def insertion_sort(arr):
    """Insertion sort implementation"""
    arr_copy = arr.copy()
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy

# Input array
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print(f"Original array: {arr}")

# Sort using different methods
sorted_bubble = bubble_sort(arr)
sorted_selection = selection_sort(arr)
sorted_insertion = insertion_sort(arr)
sorted_builtin = sorted(arr)

print(f"Bubble sort result: {sorted_bubble}")
print(f"Selection sort result: {sorted_selection}")
print(f"Insertion sort result: {sorted_insertion}")
print(f"Built-in sort result: {sorted_builtin}")