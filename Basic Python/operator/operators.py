# Arithmetic operators
print("Arithmetic operators")
a = 10
b = 3
print(f"a = {a}, b = {b}")
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Modulus (a % b):", a % b)
print("Exponentiation (a ** b):", a ** b)
print("Floor division (a // b):", a // b)
print()

# Assignment operators
print("Assignment operators")
x = 5
print(f"x = {x}")
x += 3
print("x += 3:", x)
x -= 2
print("x -= 2:", x)
x *= 2
print("x *= 2:", x)
x /= 4
print("x /= 4:", x)
x %= 2
print("x %= 2:", x)
x //= 1
print("x //= 1:", x)
x **= 3
print("x **= 3:", x)

x = int(x)

x &= 1
print("x &= 1:", x)
x |= 2
print("x |= 2:", x)
x ^= 3
print("x ^= 3:", x)
x >>= 1
print("x >>= 1:", x)
x <<= 2
print("x <<= 2:", x)
print()

# Comparison operators
print("Comparison operators")
a = 10
b = 3
print(f"a = {a}, b = {b}")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print()

# Logical operators
print("Logical operators")
a = True
b = False
print(f"a = {a}, b = {b}")
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
print()

# Identity operators
print("Identity operators")
a = 10
b = 10
c = 20
print(f"a = {a}, b = {b}, c = {c}")
print("a is b:", a is b)
print("a is not c:", a is not c)
print()

# Membership operators
print("Membership operators")
a = [1, 2, 3, 4, 5]
print(f"a = {a}")
print("3 in a:", 3 in a)
print("6 not in a:", 6 not in a)
print()

# Bitwise operators
print("Bitwise operators")
a = 10  # 1010 in binary
b = 4   # 0100 in binary
print(f"a = {a}, b = {b}")
print("a & b:", a & b)  # 0000 in binary
print("a | b:", a | b)  # 1110 in binary
print("a ^ b:", a ^ b)  # 1110 in binary
print("~a:", ~a)  # -11 in decimal (2's complement)
print("a << 2:", a << 2)  # 101000 in binary
print("a >> 2:", a >> 2)  # 0010 in binary
