"""
File Name : set_complete_guide.py
Topic     : Python Sets (Complete Guide)
Level     : Beginner → Intermediate
Purpose   : Understand set creation, properties, operations, and real-world use
"""

# =================================================
# 1. BASIC SYNTAX & CREATION OF SETS
# =================================================

# Empty set (IMPORTANT: {} creates an empty dictionary, not a set)
empty_set = set()

# Set with integers
numbers = {1, 2, 3, 4, 5}

# Set with mixed data types
mixed_set = {1, "hello", 3.14, True}

# Creating a set from a list (duplicates are removed automatically)
from_list = set([1, 2, 2, 3, 3, 4])

print("Numbers set:", numbers)
print("Set created from list:", from_list)
print("Type of numbers:", type(numbers))

print("--------------------------------")

# =================================================
# 2. REAL-WORLD USE CASES OF SETS
# =================================================

# Example 1: Remove duplicate emails
emails = ["a@mail.com", "b@mail.com", "a@mail.com"]
unique_emails = set(emails)
print("Unique emails:", unique_emails)

# Example 2: Find common interests
person1_hobbies = {"reading", "gaming", "coding"}
person2_hobbies = {"gaming", "music", "coding"}
common_hobbies = person1_hobbies & person2_hobbies
print("Common hobbies:", common_hobbies)

# Example 3: Fast membership checking
valid_users = {"alice", "bob", "charlie"}
if "alice" in valid_users:   # Very fast lookup
    print("Valid user found")

print("--------------------------------")

# =================================================
# 3. ADDING ELEMENTS TO A SET
# =================================================

set1 = {1, 2, 3, 4}

# add(): Add a single element
set1.add(5)
print("After add(5):", set1)

# update(): Add multiple elements from iterable
set1.update([6, 7, 8])
print("After update([6,7,8]):", set1)

print("--------------------------------")

# =================================================
# 4. REMOVING ELEMENTS FROM A SET
# =================================================

# remove(): Removes element, raises error if not found
set1.remove(8)

# discard(): Removes element, no error if not found
set1.discard(100)

print("After remove & discard:", set1)

print("--------------------------------")

# =================================================
# 5. SET OPERATIONS
# =================================================

set2 = {3, 4, 5, 6}

# Union - All unique elements from both sets
union_set = set1 | set2
print("Union:", union_set)

# Intersection - Common elements
intersection_set = set1 & set2
print("Intersection:", intersection_set)

# Difference - Elements in set1 but not in set2
difference_set = set1 - set2
print("Difference (set1 - set2):", difference_set)

# Symmetric Difference - Elements in either set, but not both
sym_diff = set1 ^ set2
print("Symmetric Difference:", sym_diff)

print("--------------------------------")

# =================================================
# 6. SUBSET, SUPERSET & DISJOINT
# =================================================

small_set = {1, 2}
large_set = {1, 2, 3, 4}

# issubset(): Check if all elements are in another set
print("Is subset:", small_set.issubset(large_set))

# issuperset(): Check if it contains all elements of another set
print("Is superset:", large_set.issuperset(small_set))

# isdisjoint(): Check if no elements are common
set_a = {1, 2, 3}
set_b = {4, 5, 6}
print("Is disjoint:", set_a.isdisjoint(set_b))
