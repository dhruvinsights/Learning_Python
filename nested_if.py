"""
File Name : conditional_statements_practice.py
Topic     : Python Conditional Statements (Practice Set)
Concepts  : if, if-else, if-elif-else, nested if, logical conditions
"""

# =================================================
# Question 4: Grade Calculation
# =================================================
# Assign grades based on percentage:
# >= 90 : A
# >= 80 : B
# >= 70 : C
# >= 60 : D
# <  60 : F

percentage = 88

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

# =================================================
# Question 5: Ticket Pricing System
# =================================================
# Rules:
# Age < 12        → Child Ticket
# Age 12–59       → Adult Ticket
# Age 60 or above → Senior Citizen Ticket

age = 65

if age < 12:
    print("Child Ticket")
elif age < 60:
    print("Adult Ticket")
else:
    print("Senior Citizen Ticket")

# =================================================
# Question 6: Login System
# =================================================
# Check if both username AND password are correct.
# Use nested if for clarity.

username = "user123"
password = "password123"

if username == "user123":
    if password == "password123":
        print("Login Successful")
    else:
        print("Invalid Credentials")
else:
    print("Invalid Credentials")

# =================================================
# Question 7: Discount System
# =================================================
# Discount Rules:
# Purchase > 5000  → 20%
# Purchase > 3000  → 15%
# Purchase > 1000  → 10%
# Member bonus     → +5%

purchase_amount = 4500
is_member = True
final_discount_percent = 0

if purchase_amount > 5000:
    final_discount_percent = 20
elif purchase_amount > 3000:
    final_discount_percent = 15
elif purchase_amount > 1000:
    final_discount_percent = 10
else:
    final_discount_percent = 0

# Extra discount for members
if is_member:
    final_discount_percent += 5

discount_amount = purchase_amount * (final_discount_percent / 100)
final_price = purchase_amount - discount_amount

print("Final Price after discount: $", final_price)
print("Total Discount Applied:", final_discount_percent, "%")

# =================================================
# Question 8: Income Tax Calculator
# =================================================
# Tax Slabs:
# Up to 2.5L         → No Tax
# 2.5L – 5L          → 5%
# 5L – 10L           → 20%
# Above 10L          → 30%

income = 750000
tax_amount = 0

if income <= 250000:
    tax_amount = 0
elif income <= 500000:
    tax_amount = (income - 250000) * 0.05
elif income <= 1000000:
    tax_amount = (250000 * 0.05) + (income - 500000) * 0.20
else:
    tax_amount = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("Tax payable: $", tax_amount)
