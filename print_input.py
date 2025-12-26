# Simple print
print("Hello, World!")  # Output: Hello, World!

# Print variables
name = "Dhruv"
print(name)  # Output: Dhruv

# Print multiple items
age = 20
print("Name:", name, "Age:", age)  # Output: Name: Dhruv Age: 20

# Default separator (space)
print("Python", "is", "awesome")  # Output: Python is awesome

# Custom separator
print("Python", "is", "awesome", sep="-")  # Output: Python-is-awesome

# No separator
print("Hello", "World", sep="")  # Output: HelloWorld

# Multiple character separator
print("2024", "12", "26", sep="/")  # Output: 2024/12/26


# Default end (newline)
print("Hello")
print("World")
# Output:
# Hello
# World

# Custom end - print on same line
print("Hello", end=" ")
print("World")  # Output: Hello World

# No newline
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
print()  # Add newline after loop


Section 4: Print with f-strings (Formatted Strings)

F-strings are the modern, clean way to format output. Put 'f' before the string and use {} for variables.

# Basic f-string
name = "Dhruv"
age = 20
print(f"My name is {name} and I am {age} years old")
# Output: My name is Dhruv and I am 20 years old

# F-string with expressions
x = 10
y = 5
print(f"{x} + {y} = {x + y}")  # Output: 10 + 5 = 15

# F-string with formatting
price = 49.99898989
print(f"Price: ${price:.2f}")  # Output: Price: $49.99 or $50.00

# F-string with alignment
name = "Python"
print(f"{name:>10}")   # Right align: "    Python"
print(f"{name:<10}")   # Left align: "Python    "
print(f"{name:^10}")   # Center: "  Python  "


Section 5: Print with .format() Method

The older way to format strings, still widely used.

# Basic format
name = "Dhruv"
age = 20
print("Name: {}, Age: {}".format(name, age))
# Output: Name: Dhruv, Age: 20

# Positional arguments
print("{0} + {1} = {2}".format(5, 3, 5+3))
# Output: 5 + 3 = 8

# Named arguments
print("Hello {name}, you are {age} years old".format(name="Alice", age=25))
# Output: Hello Alice, you are 25 years old


Section 6: Special Print Tricks

Trick 1: Print without newline in loop

for i in range(1, 6):
    print(i, end=" ")
print()  # Output: 1 2 3 4 5


Trick 2: Print to a file

print("Hello", file=open("output.txt", "w"))
# Writes "Hello" to output.txt file


Trick 3: Print with multiple lines

print("""Line 1
Line 2
Line 3""")
# Output:
# Line 1
# Line 2
# Line 3


Trick 4: Print special characters

print("Hello\nWorld")    # \n = newline
print("Hello\tWorld")    # \t = tab
print("Hello\\World")    # \\ = backslash
print("He said \"Hi\"")  # \" = quote


Section 7: The input() Function - Taking User Input

The input() function pauses your program and waits for the user to type something. It always returns a string.

Basic Input Syntax:

# Simple input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Output:
# Enter your name: Dhruv
# Hello, Dhruv!


Section 8: Input with Type Conversion

Since input() always returns a string, you need to convert it for numbers.

# Taking integer input
age = int(input("Enter your age: "))
print(f"Next year you'll be {age + 1}")

# Taking float input
height = float(input("Enter your height in meters: "))
print(f"Your height is {height}m")

# Taking multiple inputs in one line
x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print(f"Sum: {x + y}")

# Shorter way
x, y = map(int, input("Enter two numbers: ").split())
print(f"Sum: {x + y}")


Section 9: Input Validation Tricks

# Check if input is a number
user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
    print(f"You entered: {number}")
else:
    print("That's not a valid number!")

# Keep asking until valid input
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Please enter a valid number!")
print(f"Your age is {age}")
