"""
File Name: if_statements_complete.py
Topic    : Conditional Statements in Python
Concepts : if, if-else, if-elif-else, nested if
"""

# -------------------------------------------------
# 1. SIMPLE IF STATEMENT
# -------------------------------------------------
# A simple if statement executes code only when
# the given condition is True.

age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")

# -------------------------------------------------
# 2. IF - ELSE STATEMENT
# -------------------------------------------------
# if-else executes one block when condition is True
# and another block when condition is False.

temperature = 15

if temperature > 30:
    print("It's hot outside")
else:
    print("It's pleasant weather")

# -------------------------------------------------
# 3. IF - ELIF - ELSE STATEMENT
# -------------------------------------------------
# Used when multiple conditions need to be checked.
# Only one block will execute.

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)

# -------------------------------------------------
# 4. NESTED IF STATEMENT
# -------------------------------------------------
# An if statement inside another if statement
# is called a nested if.

has_license = True
age = 22

if age >= 18:
    print("Age requirement met")
    if has_license:
        print("You can drive")
    else:
        print("Please get a license first")
else:
    print("You are too young to drive")

# =================================================
# PRACTICE QUESTIONS WITH SOLUTIONS
# =================================================

# -------------------------------------------------
# Question 1: Age Checking
# -------------------------------------------------
# Print "Adult" if age is 18 or above,
# otherwise print "Minor".

age = 25

if age >= 18:
    print("Adult")
else:
    print("Minor")

# -------------------------------------------------
# Question 2: Even or Odd
# -------------------------------------------------
# Check whether a number is even or odd.
# Even numbers are divisible by 2.

number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# -------------------------------------------------
# Question 3: Pass or Fail
# -------------------------------------------------
# Print "Pass" if marks are 40 or above,
# otherwise print "Fail".

marks = 45

if marks >= 40:
    print("Pass")
else:
    print("Fail")
