# WHILE loop example
count = 1
print("Counting with WHILE loop:")
while count <= 5:
    print(count)
    count += 1  # This makes count increase

# BREAK statement - exit loop immediately
print("\nFinding first number divisible by 7:")
for num in range(1, 50):
    if num % 7 == 0:
        print("Found:", num)
        break  # Stop searching after finding first one

# CONTINUE statement - skip current iteration
print("\nOdd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

# PASS statement - placeholder (does nothing)
for num in range(5):
    if num == 3:
        pass  # Will implement logic later
    else:
        print(num)

# ELSE with loop - runs when loop completes normally
print("\nSearching for number 15:")
for num in range(1, 10):
    if num == 15:
        print("Found 15")
        break
else:
    print("15 not found in range")



"""
File Name : while_loop_practice_complete.py
Topic     : While Loop Practice Programs
Level     : Beginner → Advanced
Concepts  : while loop, number logic, condition checking
"""

# =================================================
# Question 1: Print numbers from 1 to 10
# =================================================
# Use while loop to print numbers from 1 to 10

count = 1
while count <= 10:
    print(count, end="")
    count += 1

print("\n--------------------------------")

# Expected Output:
# 12345678910


# =================================================
# Question 2: Sum of digits of a number
# =================================================
# Example: 1234 → 1 + 2 + 3 + 4 = 10

number = 1234
original_number = number
sum_of_digits = 0

while number > 0:
    digit = number % 10       # Get last digit
    sum_of_digits += digit    # Add digit to sum
    number //= 10             # Remove last digit

print(f"Sum of digits of {original_number}: {sum_of_digits}")

print("--------------------------------")

# Expected Output:
# Sum of digits of 1234: 10


# =================================================
# Question 4: Find the largest digit in a number
# =================================================
# Example: 4729 → 9

number = 4729
original_number = number
largest_digit = 0

while number > 0:
    digit = number % 10
    if digit > largest_digit:
        largest_digit = digit
    number //= 10

print(f"Largest digit in {original_number}: {largest_digit}")

print("--------------------------------")

# Expected Output:
# Largest digit in 4729: 9


# =================================================
# Question 5: Reverse a number
# =================================================
# Example: 1234 → 4321

number = 1234
original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(f"Reversed number of {original_number}: {reversed_number}")

print("--------------------------------")

# Expected Output:
# Reversed number of 1234: 4321


# =================================================
# Question 6: Check if a number is Palindrome
# =================================================
# A palindrome reads the same forwards and backwards

num = 12321
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")

print("--------------------------------")

# Expected Output:
# 12321 is a palindrome.


# =================================================
# Question 8: Number Guessing Game
# =================================================
# User guesses until correct number is found

import random

secret_number = random.randint(1, 100)
guess = 0

print("Guess a number between 1 and 100.")

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {secret_number}!")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("--------------------------------")


# =================================================
# Question 10: Armstrong Number
# =================================================
# Example: 153 → 1³ + 5³ + 3³ = 153

num = 153
original_num = num
sum_of_powers = 0

num_digits = len(str(num))
temp_num = num

while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits
    temp_num //= 10

if original_num == sum_of_powers:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")

# Expected Output:
# 153 is an Armstrong number.


