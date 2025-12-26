Example 1: Read entire file

# Create a sample file first
with open("story.txt", "w") as file:
    file.write("Once upon a time\n")
    file.write("There was a programmer\n")
    file.write("Who loved Python")

# Read entire file
with open("story.txt", "r") as file:
    content = file.read()
    print(content)
    print(f"\nType: {type(content)}")

# Output:
# Once upon a time
# There was a programmer
# Who loved Python
#
# Type: <class 'str'>

Example 2: Read specific number of characters

with open("story.txt", "r") as file:
    # Read first 10 characters
    first_10 = file.read(10)
    print(f"First 10 chars: '{first_10}'")
    
    # Read next 15 characters
    next_15 = file.read(15)
    print(f"Next 15 chars: '{next_15}'")

# Output:
# First 10 chars: 'Once upon '
# Next 15 chars: 'a time
# There w'

When to use read():

 Small files that fit in memory

 Need entire content as one string

 Processing the whole file at once

 Large files (can cause memory issues)

Section 3: The readline() Method - Read One Line

What it does: Reads ONE line at a time (including the newline character \n).

Syntax: file.readline()

Visual Memory Aid: "Think of readline() as eating pizza slice by slice! "

Example 1: Read lines one by one

with open("story.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    
    print(f"Line 1: {line1}")
    print(f"Line 2: {line2}")
    print(f"Line 3: {line3}")

# Output:
# Line 1: Once upon a time
#
# Line 2: There was a programmer
#
# Line 3: Who loved Python

Example 2: Read all lines using loop

with open("story.txt", "r") as file:
    line_number = 1
    while True:
        line = file.readline()
        if not line:  # Empty string means end of file
            break
        print(f"{line_number}: {line.strip()}")
        line_number += 1

# Output:
# 1: Once upon a time
# 2: There was a programmer
# 3: Who loved Python

Example 3: Read first N lines

with open("story.txt", "r") as file:
    # Read first 2 lines only
    for i in range(2):
        line = file.readline()
        print(f"Line {i+1}: {line.strip()}")

# Output:
# Line 1: Once upon a time
# Line 2: There was a programmer

When to use readline():

 Large files (memory efficient)

 Process one line at a time

 Stop reading after finding something

 Read specific number of lines

Section 4: The readlines() Method - Read All Lines as List

What it does: Reads ALL lines and returns them as a LIST of strings.

Syntax: file.readlines()

Visual Memory Aid: "Think of readlines() as getting all pizza slices in a box! "

Example 1: Read all lines as list

with open("story.txt", "r") as file:
    lines = file.readlines()
    print(f"Type: {type(lines)}")
    print(f"Number of lines: {len(lines)}")
    print(f"\nAll lines: {lines}")

# Output:
# Type: <class 'list'>
# Number of lines: 3
#
# All lines: ['Once upon a time\n', 'There was a programmer\n', 'Who loved Python']

Example 2: Process each line from list

with open("story.txt", "r") as file:
    lines = file.readlines()
    
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

# Output:
# Line 1: Once upon a time
# Line 2: There was a programmer
# Line 3: Who loved Python

Example 3: Filter specific lines

with open("story.txt", "r") as file:
    lines = file.readlines()
    
    # Find lines containing "Python"
    python_lines = [line.strip() for line in lines if "Python" in line]
    print("Lines with 'Python':", python_lines)

# Output:
# Lines with 'Python': ['Who loved Python']
