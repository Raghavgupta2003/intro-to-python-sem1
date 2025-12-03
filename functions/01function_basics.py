# ------------------------------------------------------------
# 1. Simple function (display)
# ------------------------------------------------------------
def display():
    print("I am a function")

display()


# ------------------------------------------------------------
# 2. Function without parameters
# ------------------------------------------------------------
def lang():
    print("Python is a high level language")

lang()


# ------------------------------------------------------------
# 3. Function with parameters and return type
# ------------------------------------------------------------
def sum(a: int, b: int):
    c = a + b
    return c

# Driver code
a, b = 10, 20
d = sum(a, b)
print("Sum =", d)


# ------------------------------------------------------------
# 4. Define functions for arithmetic operations
# ------------------------------------------------------------
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

def mod(x, y):
    return x % y

def floordivision(x, y):
    return x // y

def mul(x, y):
    return x * y

# Calling functions
print("Modulus =", mod(x, y))
print("Floor Division =", floordivision(x, y))
print("Multiplication =", mul(x, y))
