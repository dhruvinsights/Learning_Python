"""
File Name : functions_complete_guide.py
Topic     : Python Functions (Complete Guide)
Level     : Beginner → Intermediate
Purpose   : Understand function syntax, types, real-life examples, and parameters
"""

# =================================================
# SECTION 2: FUNCTION SYNTAX
# =================================================

# Basic function syntax
def function_name(parameters):
    """
    Docstring:
    Describes what the function does
    """
    # Function body
    result = parameters
    return result  # return is optional


# Function call
function_name("example")

# -------------------------------------------------
# Parts of a Function:
# def          → keyword to define a function
# function_name → name of the function
# parameters   → input values (optional)
# docstring    → description (optional but recommended)
# function body → code to execute
# return       → output value (optional)
# -------------------------------------------------

print("--------------------------------")

# =================================================
# SECTION 3: TYPES OF FUNCTIONS
# =================================================

# Type 1: Function without parameters and return
def greet():
    print("Hello, World!")
    print("Welcome to Python!")

greet()

print("--------------------------------")

# Type 2: Function with parameters, no return
def greet_person(name):
    print(f"Hello, {name}!")
    print("Welcome to Python!")

greet_person("Dhruv")

print("--------------------------------")

# Type 3: Function with parameters and return
def add_numbers(a, b):
    result = a + b
    return result

print(add_numbers(5, 3))
print(add_numbers(10, 20))

print("--------------------------------")

# Type 4: Function with multiple return values
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication

add, sub, mul = calculate(10, 5)
print(f"Add: {add}, Sub: {sub}, Mul: {mul}")

print("--------------------------------")

# =================================================
# SECTION 4: REAL-LIFE EXAMPLES
# =================================================

# Example 1: Calculator Function
def calculator(num1, num2, operation):
    """Performs basic arithmetic operations"""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "*"))

print("--------------------------------")

# Example 2: Grade Calculator
def calculate_grade(marks):
    """Returns grade based on marks"""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

student_marks = 85
print(f"Grade: {calculate_grade(student_marks)}")

print("--------------------------------")

# Example 3: Temperature Converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5 / 9

temp_c = 25
print(f"{temp_c}°C = {celsius_to_fahrenheit(temp_c)}°F")

print("--------------------------------")

# Example 4: Email Validator
def is_valid_email(email):
    """Check if email format is valid"""
    if "@" in email and "." in email:
        parts = email.split("@")
        if len(parts) == 2 and parts[0] and parts[1]:
            return True
    return False

print(is_valid_email("dhruv@example.com"))
print(is_valid_email("invalid.email"))

print("--------------------------------")

# Example 5: List Operations
def find_max_min(numbers):
    """Return maximum and minimum from list"""
    if not numbers:
        return None, None
    return max(numbers), min(numbers)

nums = [45, 23, 67, 12, 89, 34]
maximum, minimum = find_max_min(nums)
print(f"Max: {maximum}, Min: {minimum}")

print("--------------------------------")

# =================================================
# SECTION 5: FUNCTION PARAMETERS
# =================================================

# Default parameters
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Dhruv")
greet("Dhruv", "Hi")

print("--------------------------------")

# Keyword arguments
def student_info(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student_info(age=20, name="Dhruv", grade="A")

print("--------------------------------")

# Variable-length arguments (*args)
def sum_all(*numbers):
    """Sum any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40))

print("--------------------------------")

# Keyword variable-length arguments (**kwargs)
def display_info(**info):
    """Display key-value pairs"""
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Dhruv", age=20, city="Delhi")


"""
File Name : file_operations_basic_guide.py
Topic     : Basic File Operations in Python
Sections  : Writing files, Reading files, with statement (best practice)
Level     : Beginner
"""

# =================================================
# SECTION 6: BASIC FILE OPERATIONS
# =================================================

# Example 1: Creating and Writing to a File
# -----------------------------------------
# open("filename", "w") → Opens file in write mode
# If file does not exist → it is created
# If file exists → content is overwritten

file = open("student.txt", "w")
file.write("Name: Dhruv\n")
file.write("Age: 20\n")
file.write("Course: Python Programming")
file.close()   # IMPORTANT: Close the file after writing

print("File created and written successfully!")

print("--------------------------------")

# Example 2: Reading from a File
# ------------------------------
# open("filename", "r") → Opens file in read mode

file = open("student.txt", "r")
content = file.read()   # Read entire file content
print("File content:")
print(content)
file.close()   # Always close the file after reading

# Expected Output:
# Name: Dhruv
# Age: 20
# Course: Python Programming

print("--------------------------------")

# =================================================
# SECTION 7: THE 'with' STATEMENT (BEST PRACTICE)
# =================================================

# The 'with' statement automatically closes the file
# even if an error occurs.
# This is the RECOMMENDED way to work with files.

# ❌ Old Way (Manual Close - Error Prone)
file = open("student.txt", "r")
content = file.read()
file.close()   # Must remember to close manually

print("Reading using old way:")
print(content)

print("--------------------------------")

# ✅ Better Way (Automatic Close using with)
with open("student.txt", "r") as file:
    content = file.read()
    # File is open ONLY inside this block

# File is automatically closed here (outside block)

print("Reading using 'with' statement:")
print(content)
