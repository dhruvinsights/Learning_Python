"""
File Name : pattern_printing_complete.py
Topic     : Pattern Printing using Nested Loops
Concepts  : for loop, nested loop, range(), logic building
"""

# =================================================
# Example 1: Simple Pattern (Right Triangle)
# =================================================
# Pattern:
# *
# **
# ***
# ****
# *****

# Logic:
# - Total rows = 5
# - Stars in each row = row number

rows = 5

for i in range(1, rows + 1):      # Outer loop controls rows
    for j in range(i):            # Inner loop prints stars
        print("*", end="")
    print()                       # Move to next line

print("--------------------------------")

# =================================================
# Example 2: Intermediate Pattern (Pyramid)
# =================================================
# Pattern:
#     *
#    ***
#   *****
#  *******
# *********

# Logic:
# - Total rows = 5
# - Spaces = rows - i
# - Stars  = 2*i - 1 (odd numbers)

rows = 5

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()   # New line after each row

print("--------------------------------")

# =================================================
# Example 3: Complex Pattern (Diamond)
# =================================================
# Pattern:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# Logic:
# - Diamond = Pyramid + Inverted Pyramid
# - Upper half increases
# - Lower half decreases

rows = 5

# -------- Upper Half (Pyramid) --------
for i in range(1, rows + 1):
    # Spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()

# -------- Lower Half (Inverted Pyramid) --------
for i in range(rows - 1, 0, -1):
    # Spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()
