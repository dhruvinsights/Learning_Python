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
