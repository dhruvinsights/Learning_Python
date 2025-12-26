"""
File Name : list_methods_complete_demo.py
Topic     : Python List Methods & List Slicing
Level     : Beginner
"""

# =================================================
# 1. ADDING ELEMENTS TO A LIST
# =================================================

fruits = ["apple", "banana", "cherry"]
print("Original fruits list:", fruits)

# append(): Adds an element to the end of the list
fruits.append("date")
print("After append('date'):", fruits)

# extend(): Adds multiple elements from another list
more_fruits = ["elderberry", "fig"]
fruits.extend(more_fruits)
print("After extend(['elderberry', 'fig']):", fruits)

# insert(): Adds an element at a specific index
fruits.insert(1, "apricot")
print("After insert(1, 'apricot'):", fruits)

print("--------------------------------")

# =================================================
# 2. REMOVING ELEMENTS FROM A LIST
# =================================================

print("Current fruits list:", fruits)

# remove(): Removes first occurrence of given value
fruits.remove("banana")
print("After remove('banana'):", fruits)

# pop(): Removes and returns last element
last_item = fruits.pop()
print("Removed using pop():", last_item)
print("List after pop():", fruits)

# pop(index): Removes element at specific index
first_item = fruits.pop(0)
print("Removed using pop(0):", first_item)
print("List after pop(0):", fruits)

# clear(): Removes all elements
temp_list = ["a", "b", "c"]
temp_list.clear()
print("After clear():", temp_list)

print("--------------------------------")

# =================================================
# 3. SORTING & REVERSING LISTS
# =================================================

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Original numbers list:", numbers)

# sort(): Sorts list in ascending order (in-place)
numbers.sort()
print("After sort():", numbers)

# reverse(): Reverses list order
numbers.reverse()
print("After reverse():", numbers)

# sorted(): Returns a new sorted list (original unchanged)
unsorted_numbers = [3, 1, 4, 2]
new_sorted_list = sorted(unsorted_numbers)
print("Original list for sorted():", unsorted_numbers)
print("New list from sorted():", new_sorted_list)

print("--------------------------------")

# =================================================
# 4. COPYING LISTS
# =================================================

original_list = [10, 20, 30]
print("Original list:", original_list)

# copy(): Creates a shallow copy
copied_list = original_list.copy()
original_list.append(40)

print("Original list after append:", original_list)
print("Copied list (unchanged):", copied_list)

print("--------------------------------")

# =================================================
# 5. LIST INFORMATION METHODS
# =================================================

current_list = ["a", "b", "c", "d"]

# len(): Returns number of elements
print("Length of current_list:", len(current_list))

# index(): Returns index of first occurrence
print("Index of 'b':", current_list.index("b"))

# count(): Returns number of occurrences
numbers = [1, 2, 1, 3, 1, 4]
print("Count of 1:", numbers.count(1))

print("--------------------------------")

# =================================================
# 6. LIST SLICING
# =================================================

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
print("Colors list:", colors)

# [start:end]
print("Slice [1:4]:", colors[1:4])

# [:end]
print("Slice [:3]:", colors[:3])

# [start:]
print("Slice [2:]:", colors[2:])

# [::step]
print("Slice [::2]:", colors[::2])

# Reverse list using slicing
print("Slice [::-1]:", colors[::-1])
