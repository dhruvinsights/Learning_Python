"""
File Name : advanced_dictionary_techniques.py
Topic     : Advanced Dictionary Techniques in Python
Level     : Intermediate → Advanced
Purpose   : Master real-world dictionary usage
"""

# =================================================
# Technique 1: Merging Dictionaries
# =================================================

# Method 1: Using update()  (modifies original dictionary)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print("Merged using update():", dict1)

# Method 2: Using ** unpacking (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}
print("Merged using ** operator:", merged)

# Method 3: Using | operator (Python 3.9+)
merged_pipe = dict1 | dict2
print("Merged using | operator:", merged_pipe)

print("--------------------------------")

# =================================================
# Technique 2: Dictionary Comprehension
# =================================================

# Create dictionary from list
numbers = [1, 2, 3, 4, 5]
squares = {num: num ** 2 for num in numbers}
print("Squares dictionary:", squares)

# Filter dictionary
scores = {"math": 85, "english": 92, "science": 78, "history": 95}
high_scores = {sub: score for sub, score in scores.items() if score >= 90}
print("Filtered scores:", high_scores)

# Transform values
prices = {"apple": 50, "banana": 30, "orange": 40}
discounted = {item: price * 0.9 for item, price in prices.items()}
print("Discounted prices:", discounted)

print("--------------------------------")

# =================================================
# Technique 3: Inverting Dictionary (Swap Keys & Values)
# =================================================

# Simple inversion (values must be unique)
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print("Inverted dictionary:", inverted)

# Handling duplicate values
original = {"a": 1, "b": 2, "c": 1}
inverted = {}

for key, value in original.items():
    if value not in inverted:
        inverted[value] = []
    inverted[value].append(key)

print("Inverted with duplicates:", inverted)

print("--------------------------------")

# =================================================
# Technique 4: Nested Dictionary Access
# =================================================

student = {
    "name": "Dhruv",
    "marks": {
        "math": 85,
        "science": 90
    }
}

# Direct access
print("Math marks:", student["marks"]["math"])

# Safe access using get()
print("English marks:", student.get("marks", {}).get("english", "Not found"))

print("--------------------------------")

# =================================================
# Technique 5: Sorting Dictionary
# =================================================

scores = {"math": 85, "english": 92, "science": 78}

# Sort by keys
sorted_by_key = dict(sorted(scores.items()))
print("Sorted by key:", sorted_by_key)

# Sort by values (ascending)
sorted_by_value = dict(sorted(scores.items(), key=lambda x: x[1]))
print("Sorted by value:", sorted_by_value)

# Sort by values (descending)
sorted_desc = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print("Sorted descending:", sorted_desc)

print("--------------------------------")

# =================================================
# Technique 6: Counting with Dictionaries
# =================================================

text = "hello world"
frequency = {}

for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

print("Character frequency:", frequency)

# Using setdefault()
frequency = {}
for char in text:
    if char != " ":
        frequency.setdefault(char, 0)
        frequency[char] += 1

print("Frequency using setdefault():", frequency)

print("--------------------------------")

# =================================================
# Technique 7: Default Dictionary Values
# =================================================

inventory = {"apple": 10, "banana": 5}

# get() with default
print("Oranges in stock:", inventory.get("orange", 0))

# setdefault()
inventory.setdefault("orange", 0)
print("Inventory after setdefault():", inventory)

print("--------------------------------")

# =================================================
# Technique 8: Removing Items While Iterating (Safe Way)
# =================================================

scores = {"math": 85, "english": 92, "science": 78}

# Iterate over copy of keys
for subject in list(scores.keys()):
    if scores[subject] < 80:
        del scores[subject]

print("After safe removal:", scores)
