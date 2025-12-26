"""
File Name : file_writing_complete_guide.py
Topic     : Writing Files in Python (write, writelines, append)
Level     : Beginner → Intermediate
Purpose   : Understand how data is written to files with real-world examples
"""

# =================================================
# EXAMPLE 1: BASIC WRITE (NO NEWLINE)
# =================================================
# write() does NOT automatically add a newline

with open("output.txt", "w") as file:
    file.write("Hello, World!")
    file.write("Python is awesome")

with open("output.txt", "r") as file:
    print(file.read())

# Output:
# Hello, World!Python is awesome

print("--------------------------------")

# =================================================
# EXAMPLE 2: WRITE WITH NEWLINES
# =================================================

with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python is awesome\n")
    file.write("File handling is easy")

with open("output.txt", "r") as file:
    print(file.read())

print("--------------------------------")

# =================================================
# EXAMPLE 3: write() RETURNS CHARACTER COUNT
# =================================================

with open("output.txt", "w") as file:
    chars_written = file.write("Hello, World!")
    print(f"Characters written: {chars_written}")

print("--------------------------------")

# =================================================
# EXAMPLE 4: WRITING NUMBERS (STRING CONVERSION REQUIRED)
# =================================================

with open("numbers.txt", "w") as file:
    file.write(str(123) + "\n")
    file.write(str(456) + "\n")
    file.write(str(789))

with open("numbers.txt", "r") as file:
    print(file.read())

print("--------------------------------")

# =================================================
# SECTION 4: writelines() METHOD
# =================================================
# writelines() writes a list of strings
# IMPORTANT: It does NOT add newline automatically

# Example 1: Correct usage with newlines
lines = ["Apple\n", "Banana\n", "Cherry\n", "Date"]

with open("fruits.txt", "w") as file:
    file.writelines(lines)

with open("fruits.txt", "r") as file:
    print(file.read())

print("--------------------------------")

# Example 2: Common mistake (no newlines)
lines = ["Apple", "Banana", "Cherry"]

with open("fruits.txt", "w") as file:
    file.writelines(lines)

with open("fruits.txt", "r") as file:
    print(file.read())

print("--------------------------------")

# Example 3: Adding newlines properly

fruits = ["Apple", "Banana", "Cherry", "Date"]

# Method 1: List comprehension
lines_with_newline = [fruit + "\n" for fruit in fruits]
with open("fruits.txt", "w") as file:
    file.writelines(lines_with_newline)

# Method 2: Loop with write()
with open("fruits2.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

print("--------------------------------")

# =================================================
# VISUAL COMPARISON: write() vs writelines()
# =================================================

# Using write()
with open("method1.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

# Using writelines()
with open("method2.txt", "w") as file:
    file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])

# Both files will have identical content

print("--------------------------------")

# =================================================
# SECTION 6: PRACTICAL EXAMPLES
# =================================================

# Example 1: Save user data
name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")

with open("user_data.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"City: {city}\n")

print("User data saved successfully!")

print("--------------------------------")

# Example 2: Create a log file (append mode)
from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")

log_message("Application started")
log_message("User logged in")
log_message("Data processed successfully")

print("Log file updated!")

print("--------------------------------")

# Example 3: Save list to file with numbering
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

with open("students.txt", "w") as file:
    for i, student in enumerate(students, 1):
        file.write(f"{i}. {student}\n")

print("Students list saved!")

print("--------------------------------")

# Example 4: Copy file content
with open("source.txt", "r") as source:
    content = source.read()

with open("destination.txt", "w") as dest:
    dest.write(content)

print("File copied successfully!")

print("--------------------------------")

# Example 5: Write dictionary to file
student = {
    "name": "Dhruv",
    "age": 20,
    "grade": "A",
    "subjects": ["Python", "Math", "Physics"]
}

with open("student_info.txt", "w") as file:
    for key, value in student.items():
        file.write(f"{key}: {value}\n")

print("Student information saved!")

print("--------------------------------")

# =================================================
# SECTION 7: COMMON FILE WRITING PATTERNS
# =================================================

# Pattern 1: Read → Modify → Write
with open("data.txt", "r") as file:
    lines = file.readlines()

modified_lines = [line.upper() for line in lines]

with open("data.txt", "w") as file:
    file.writelines(modified_lines)

print("File modified successfully!")

print("--------------------------------")

# Pattern 2: Append with timestamp
with open("events.txt", "a") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] New event occurred\n")

print("Event logged!")

print("--------------------------------")

# Pattern 3: Write CSV-like data
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "London"],
    ["Charlie", "28", "Paris"]
]

with open("data.csv", "w") as file:
    for row in data:
        file.write(",".join(row) + "\n")

print("CSV file created!")
