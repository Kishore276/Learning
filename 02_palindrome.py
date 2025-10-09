# Palindrome Checker (String and Number)

def is_palindrome_string(s):
    """Check if a string is palindrome"""
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

def is_palindrome_number(n):
    """Check if a number is palindrome"""
    str_n = str(n)
    return str_n == str_n[::-1]

def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

# Check palindrome for string
text = input("Enter a string to check if it's palindrome: ")
if is_palindrome_string(text):
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")

# Check palindrome for number
number = int(input("Enter a number to check if it's palindrome: "))
if is_palindrome_number(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")

# Demonstrate string reversal
sample_string = input("Enter a string to reverse: ")
reversed_str = reverse_string(sample_string)
print(f"Original: {sample_string}")
print(f"Reversed: {reversed_str}")