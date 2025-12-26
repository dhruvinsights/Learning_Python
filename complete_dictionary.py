"""
File Name : dictionary_methods_complete_guide.py
Topic     : Python Dictionary Methods & Built-in Functions
Level     : Beginner → Intermediate
Purpose   : Learn how to access, modify, remove, copy, and analyze dictionaries
"""

# =================================================
# 1. ACCESSING DICTIONARY DATA
# =================================================

student_profile = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# get(): Safely retrieves value by key
major = student_profile.get("major")
print("Major (using get()):", major)

# get() with default value if key not found
city = student_profile.get("city", "Not Specified")
print("City (using get() with default):", city)

# keys(): Returns all keys
print("All keys:", student_profile.keys())

# values(): Returns all values
print("All values:", student_profile.values())

# items(): Returns key-value pairs as tuples
print("All items:", student_profile.items())

print("--------------------------------")

# =================================================
# 2. ADDING & UPDATING DICTIONARY ITEMS
# =================================================

student_profile = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
print("Initial student_profile:", student_profile)

# update(): Update existing keys or add new keys
student_profile.update({"age": 21, "city": "New York"})
print("After update():", student_profile)

# setdefault(): Adds key if not present
email = student_profile.setdefault("email", "unknown@example.com")
print("Email (new key):", email)
print("After setdefault (new key):", student_profile)

# setdefault() on existing key does nothing
age_value = student_profile.setdefault("age", 25)
print("Age (existing key):", age_value)
print("After setdefault (existing key):", student_profile)

print("--------------------------------")

# =================================================
# 3. REMOVING DICTIONARY ITEMS
# =================================================

student_profile = {
    "name": "Bob",
    "age": 22,
    "major": "Physics",
    "gpa": 3.5,
    "city": "London"
}
print("Initial student_profile:", student_profile)

# pop(): Remove specific key and return its value
removed_gpa = student_profile.pop("gpa")
print("Removed GPA:", removed_gpa)
print("After pop('gpa'):", student_profile)

# popitem(): Removes last inserted key-value pair
last_item = student_profile.popitem()
print("Removed last item:", last_item)
print("After popitem():", student_profile)

# clear(): Remove all items
temp_dict = {"a": 1, "b": 2}
print("Before clear():", temp_dict)
temp_dict.clear()
print("After clear():", temp_dict)

print("--------------------------------")

# =================================================
# 4. COPYING DICTIONARIES & LENGTH
# =================================================

student_profile = {
    "name": "Bob",
    "age": 22,
    "major": "Physics"
}
print("Initial student_profile:", student_profile)

# copy(): Creates a shallow copy
copied_profile = student_profile.copy()

# Modify original dictionary
student_profile["age"] = 23

print("Original profile:", student_profile)
print("Copied profile:", copied_profile)

# len(): Number of key-value pairs
print("Length of student_profile:", len(student_profile))

print("--------------------------------")

# =================================================
# 5. CREATING DICTIONARY USING fromkeys()
# =================================================

keys_list = ["apple", "banana", "cherry"]

# fromkeys(): Assign same default value to all keys
fruit_counts = dict.fromkeys(keys_list, 0)
print("Fruit counts:", fruit_counts)

# fromkeys() without default value
another_dict = dict.fromkeys(["a", "b", "c"])
print("Another dict:", another_dict)

print("--------------------------------")

# =================================================
# 6. DICTIONARY BUILT-IN FUNCTIONS
# =================================================

student = {"name": "Dhruv", "age": 20, "grade": "A", "marks": 95}

# len(): Number of items
print("Length:", len(student))

# str(): Convert dictionary to string
print("String format:", str(student))

# type(): Check type
print("Type:", type(student))

# dict(): Create dictionary using keyword arguments
new_dict = dict(city="Delhi", country="India")
print("New dict:", new_dict)

print("--------------------------------")

# =================================================
# 7. SORTING, MAX, MIN, SUM ON DICTIONARY
# =================================================

scores = {"math": 85, "english": 92, "science": 78}

# sorted(): Sort dictionary keys
print("Sorted keys:", sorted(scores))

# max() & min() based on values
highest_subject = max(scores, key=scores.get)
lowest_subject = min(scores, key=scores.get)

print("Highest scoring subject:", highest_subject)
print("Lowest scoring subject:", lowest_subject)

# sum(): Sum of all values
print("Total marks:", sum(scores.values()))

print("--------------------------------")

# =================================================
# 8. any() and all() WITH DICTIONARIES
# =================================================

dict1 = {0: "zero", 1: "one"}
dict2 = {1: "one", 2: "two"}

# any(): True if any key is truthy
print("any(dict1):", any(dict1))
print("any(dict2):", any(dict2))

# all(): True only if all keys are truthy
print("all(dict1):", all(dict1))
print("all(dict2):", all(dict2))
