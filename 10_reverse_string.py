# Reverse a String

def reverse_string_slicing(s):
    """Reverse string using slicing"""
    return s[::-1]

def reverse_string_loop(s):
    """Reverse string using loop"""
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

def reverse_string_builtin(s):
    """Reverse string using built-in functions"""
    return ''.join(reversed(s))

def reverse_string_recursion(s):
    """Reverse string using recursion"""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string_recursion(s[:-1])

def reverse_words_in_string(s):
    """Reverse words in a string"""
    words = s.split()
    reversed_words = []
    for word in reversed(words):
        reversed_words.append(word)
    return ' '.join(reversed_words)

# Input string
text = input("Enter a string to reverse: ")

print(f"Original string: '{text}'")

# Reverse using different methods
reversed1 = reverse_string_slicing(text)
reversed2 = reverse_string_loop(text)
reversed3 = reverse_string_builtin(text)
reversed4 = reverse_string_recursion(text)
reversed5 = reverse_words_in_string(text)

print(f"Reversed (slicing): '{reversed1}'")
print(f"Reversed (loop): '{reversed2}'")
print(f"Reversed (built-in): '{reversed3}'")
print(f"Reversed (recursion): '{reversed4}'")
print(f"Reversed words: '{reversed5}'")