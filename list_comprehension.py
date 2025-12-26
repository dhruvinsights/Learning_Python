"""
File Name : list_comprehension_complete_guide.py
Topic     : List Comprehension in Python
Level     : Beginner → Advanced
Purpose   : Learn how to replace loops with clean one-line expressions
"""

# =================================================
# 1. Traditional Way vs List Comprehension
# =================================================

# Traditional way (multiple lines)
numbers = []
for i in range(1, 6):
    numbers.append(i)
print("Traditional way:", numbers)

# List comprehension (one line)
numbers = [i for i in range(1, 6)]
print("List comprehension:", numbers)

print("--------------------------------")

# =================================================
# 2. Basic Syntax of List Comprehension
# =================================================
# [expression for item in iterable]

# Example 1: Squares of numbers
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

# Example 2: Convert strings to uppercase
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)

# Example 3: Multiply each number by 2
numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
print("Doubled numbers:", doubled)

print("--------------------------------")

# =================================================
# 3. List Comprehension with if condition
# =================================================
# [expression for item in iterable if condition]

# Example 1: Even numbers only
numbers = list(range(1, 11))
evens = [num for num in numbers if num % 2 == 0]
print("Even numbers:", evens)

# Example 2: Words longer than 5 characters
words = ["hello", "world", "python", "programming", "code"]
long_words = [word for word in words if len(word) > 5]
print("Long words:", long_words)

# Example 3: Positive numbers only
numbers = [-5, 3, -2, 8, -1, 10]
positives = [num for num in numbers if num > 0]
print("Positive numbers:", positives)

print("--------------------------------")

# =================================================
# 4. List Comprehension with if-else
# =================================================
# [expression_if_true if condition else expression_if_false for item in iterable]

# Example 1: Replace negative numbers with 0
numbers = [-5, 3, -2, 8, -1, 10]
result = [num if num > 0 else 0 for num in numbers]
print("Negative replaced with 0:", result)

# Example 2: Label even or odd
numbers = [1, 2, 3, 4, 5]
labels = ["even" if num % 2 == 0 else "odd" for num in numbers]
print("Even/Odd labels:", labels)

# Example 3: Celsius to Fahrenheit (only if > 0)
celsius = [-5, 0, 10, 20, 30]
fahrenheit = [c * 9/5 + 32 if c > 0 else c for c in celsius]
print("Temperature conversion:", fahrenheit)

print("--------------------------------")

# =================================================
# 5. Nested List Comprehension
# =================================================

# Example 1: Create a 3x3 multiplication matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("3x3 Matrix:", matrix)

# Example 2: Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened list:", flattened)

# Example 3: Generate all possible pairs
list1 = [1, 2, 3]
list2 = ['a', 'b']
pairs = [(num, letter) for num in list1 for letter in list2]
print("All pairs:", pairs)

print("--------------------------------")

# =================================================
# 6. List Comprehension Tricks (Real-World Use)
# =================================================

# Trick 1: Remove duplicates while preserving order
numbers = [1, 2, 2, 3, 4, 3, 5, 1]
unique = []
[unique.append(x) for x in numbers if x not in unique]
print("Unique numbers:", unique)

# Trick 2: Squares of even numbers only
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print("Even squares:", even_squares)

# Trick 3: Extract first letter of each word
sentence = "Python is awesome"
first_letters = [word[0] for word in sentence.split()]
print("First letters:", first_letters)

# Trick 4: Multiple conditions
numbers = range(1, 21)
filtered = [x for x in numbers if x % 2 == 0 or x % 3 == 0]
print("Divisible by 2 or 3:", filtered)

# Trick 5: Using functions inside list comprehension
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = [square(x) for x in numbers]
print("Squared using function:", squared)
