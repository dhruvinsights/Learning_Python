"""
File Name : loops_and_builtins_demo.py
Topic     : range(), len(), enumerate(), zip(), split(), join(), strip()
Purpose   : Understanding loops and common built-in functions in Python
"""

# =================================================
# 1. range() FUNCTION WITH FOR LOOP
# =================================================

# range(stop)
# Generates numbers from 0 to stop-1
for i in range(5):
    print(i)   # Output: 0 1 2 3 4

print("------------")

# range(start, stop)
# Generates numbers from start to stop-1
for i in range(1, 6):
    print(i)   # Output: 1 2 3 4 5

print("------------")

# range(start, stop, step)
# Generates numbers with a fixed step value
for i in range(0, 11, 2):
    print(i)   # Output: 0 2 4 6 8 10

print("------------")

# Reverse counting using negative step
for i in range(10, 0, -1):
    print(i)   # Output: 10 to 1

# =================================================
# 2. len() FUNCTION
# =================================================

# Length of a string
name = "Python"
print("Length of string:", len(name))   # 6

# Length of a list
numbers = [10, 20, 30, 40, 50]
print("Length of list:", len(numbers))  # 5

print("------------")

# Using len() with loop to access list elements by index
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

# =================================================
# 3. enumerate() FUNCTION
# =================================================

fruits = ["apple", "banana", "cherry"]

# Without enumerate (index manually)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

print("------------")

# With enumerate (automatic index + value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("------------")

# enumerate with custom starting index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# =================================================
# 4. zip() FUNCTION
# =================================================

# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Looping two lists together
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

print("------------")

# Three lists together
scores = [85, 90, 78]

for name, age, score in zip(names, ages, scores):
    print(f"{name}, {age} years old, scored {score}")

# =================================================
# 5. STRING FUNCTIONS
# =================================================

# split() - converts string into list
sentence = "Python is awesome"
words = sentence.split()

for word in words:
    print(word)

print("------------")

# join() - converts list into string
words = ["Hello", "World"]
result = " ".join(words)
print(result)

print("------------")

# strip() - removes extra spaces from both ends
text = "  hello  "
print(text.strip())
