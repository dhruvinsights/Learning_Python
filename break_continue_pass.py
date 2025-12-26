"""
File Name : loop_control_statements.py
Topic     : Loop Control Statements in Python
Concepts  : break, continue, pass
"""

# =================================================
# Example 1: break statement
# =================================================
# break is used to exit the loop immediately
# when a specific condition is met.

print("Example of break:")

for i in range(1, 11):
    if i == 5:
        break          # Loop stops completely when i becomes 5
    print(i)

print("--------------------------------")

# =================================================
# Example 2: continue statement
# =================================================
# continue skips the current iteration
# and moves to the next loop iteration.

print("Example of continue:")

for i in range(1, 11):
    if i == 5:
        continue       # Skips printing 5
    print(i)

print("--------------------------------")

# =================================================
# Example 3: pass statement
# =================================================
# pass does nothing and is used as a placeholder
# when a statement is syntactically required.

print("Example of pass:")

for i in range(1, 6):
    if i == 3:
        pass           # No action taken when i is 3
    else:
        print(i)
