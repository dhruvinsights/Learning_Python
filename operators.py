# ===============================
# ALL PYTHON OPERATORS (A–Z)
# ===============================

a = 10
b = 3

print("---- Arithmetic Operators ----")
print("Addition:", a + b)          # +
print("Subtraction:", a - b)       # -
print("Multiplication:", a * b)    # *
print("Division:", a / b)          # /
print("Floor Division:", a // b)   # //
print("Modulus:", a % b)           # %
print("Exponent:", a ** b)         # **

print("\n---- Assignment Operators ----")
x = 5
print("=", x)

x += 3
print("+=", x)

x -= 2
print("-=", x)

x *= 2
print("*=", x)

x /= 2
print("/=", x)

x //= 2
print("//=", x)

x %= 2
print("%=", x)

x **= 3
print("**=", x)

x = 6
x &= 3
print("&=", x)

x |= 3
print("|=", x)

x ^= 3
print("^=", x)

x <<= 1
print("<<=", x)

x >>= 1
print(">>=", x)

print("\n---- Comparison Operators ----")
print("==", a == b)
print("!=", a != b)
print(">", a > b)
print("<", a < b)
print(">=", a >= b)
print("<=", a <= b)

print("\n---- Logical Operators ----")
print("and:", a > 5 and b > 1)
print("or:", a < 5 or b > 1)
print("not:", not (a > 5))

print("\n---- Bitwise Operators ----")
print("&:", a & b)
print("|:", a | b)
print("^:", a ^ b)
print("~a:", ~a)
print("<<:", a << 1)
print(">>:", a >> 1)

print("\n---- Membership Operators ----")
list_data = [1, 2, 3, 10]
print("in:", a in list_data)
print("not in:", b not in list_data)

print("\n---- Identity Operators ----")
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("is:", x is y)
print("is not:", x is not z)

print("\n---- Conditional (Ternary) Operator ----")
result = "Greater" if a > b else "Smaller"
print("Result:", result)

print("\n---- Operator Precedence Example ----")
result = a + b * 2 ** 2
print("a + b * 2 ** 2 =", result)
