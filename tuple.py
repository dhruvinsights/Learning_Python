"""
File Name : tuple_complete_guide.py
Topic     : Python Tuples (Complete Guide)
Level     : Beginner
Purpose   : Understand tuple creation, usage, operations, and built-in functions
"""

# =================================================
# 1. BASIC SYNTAX & CREATION OF TUPLES
# =================================================

# Empty tuple
empty_tuple = ()

# Single item tuple (comma is mandatory)
single_item = (5,)

# Tuple with multiple elements
coordinates = (10, 20)

# Mixed data types
mixed_tuple = (1, "hello", 3.14, True)

# Nested tuple
nested_tuple = (1, 2, (3, 4))

print("Coordinates:", coordinates)
print("Type of coordinates:", type(coordinates))

print("--------------------------------")

# =================================================
# 2. REAL-WORLD USE CASES OF TUPLES
# =================================================

# Coordinates (should not change)
location = (28.6139, 77.2090)  # Delhi coordinates

# RGB color (fixed values)
red = (255, 0, 0)

# Date (immutable)
date = (2024, 12, 26)  # Year, Month, Day

# Database record
student_record = (101, "Dhruv", "Computer Science", 3.8)

print("Location:", location)
print("Red color RGB:", red)
print("Date:", date)
print("Student record:", student_record)

print("--------------------------------")

# =================================================
# 3. ACCESSING & BASIC OPERATIONS ON TUPLES
# =================================================

# Creating a tuple
fruits = ("apple", "banana", "cherry", "apple")

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing
print("Slice [1:3]:", fruits[1:3])

# Length
print("Length of tuple:", len(fruits))

# Count occurrences
print("Count of 'apple':", fruits.count("apple"))

# Find index
print("Index of 'banana':", fruits.index("banana"))

print("--------------------------------")

# =================================================
# 4. TUPLE UNPACKING
# =================================================

a, b, c, d = fruits
print("Unpacked values:", a, b, c, d)

print("--------------------------------")

# =================================================
# 5. TUPLE CONCATENATION & REPETITION
# =================================================

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print("Concatenated tuple:", combined)

# Repetition
repeated = (1, 2) * 3
print("Repeated tuple:", repeated)

print("--------------------------------")

# =================================================
# 6. MEMBERSHIP OPERATORS
# =================================================

print("'apple' in fruits:", "apple" in fruits)
print("'mango' in fruits:", "mango" in fruits)

print("--------------------------------")

# =================================================
# 7. BUILT-IN FUNCTIONS WITH TUPLES
# =================================================

numbers = (5, 2, 8, 1, 9, 2)

# len()
print("Length:", len(numbers))

# max() and min()
print("Max value:", max(numbers))
print("Min value:", min(numbers))

# sum()
print("Sum:", sum(numbers))

# sorted() → returns a LIST
print("Sorted numbers:", sorted(numbers))

# tuple() → convert list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("Converted tuple:", my_tuple)

# count()
print("Count of 2:", numbers.count(2))

# index()
print("Index of 8:", numbers.index(8))

print("--------------------------------")

# =================================================
# 8. any() and all() WITH TUPLES
# =================================================

print("any((0, 0, 1)):", any((0, 0, 1)))
print("all((1, 2, 3)):", all((1, 2, 3)))
print("all((1, 0, 3)):", all((1, 0, 3)))
