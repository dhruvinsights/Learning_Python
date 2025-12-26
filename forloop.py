"""
File Name : loop_practice_programs.py
Topic     : Loop-based Programming Questions
Concepts  : for loop, range(), strings, lists, logic building
Level     : Beginner / School / College
"""

# =================================================
# Question 4: Multiplication Table
# =================================================
# Print multiplication table of a given number

number = 7
print(f"Multiplication table for {number}:")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("--------------------------------")

# =================================================
# Question 5: Count Vowels in a String
# =================================================
# Check each character and count vowels

input_string = "Programming"
vowels = "aeiouAEIOU"
count = 0

for char in input_string:
    if char in vowels:
        count += 1

print(f"Number of vowels in '{input_string}':", count)

print("--------------------------------")

# =================================================
# Question 6: Factorial of a Number
# =================================================
# Factorial of n = 1 × 2 × 3 × ... × n

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number}:", factorial)

print("--------------------------------")

# =================================================
# Question 7: Reverse a String
# =================================================
# Build reversed string character by character

input_string = "Python"
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print(f"Original string: '{input_string}'")
print(f"Reversed string: '{reversed_string}'")

print("--------------------------------")

# =================================================
# Question 8: Pattern Printing
# =================================================
# Print star pattern:
# *
# **
# ***
# ****
# *****

rows = 5

for i in range(1, rows + 1):
    print("*" * i)

print("--------------------------------")

# =================================================
# Question 9: Fibonacci Series
# =================================================
# Fibonacci series starts with 0, 1
# Next term = sum of previous two terms

n = 8
a, b = 0, 1
fib_series = []

for _ in range(n):
    fib_series.append(a)
    a, b = b, a + b

print("Fibonacci Series:", fib_series)

print("--------------------------------")

# =================================================
# Question 10: Prime Number Checker
# =================================================
# A prime number is divisible only by 1 and itself

number = 17
is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

print(f"{number} is prime:", is_prime)
