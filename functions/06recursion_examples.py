# -------------------------------------------------------------
# RECURSION PROGRAMS - FULL FILE
# -------------------------------------------------------------

# 1. FACTORIAL USING RECURSION
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

num = 3
print("factorial of", num, "=", fact(num))



# -------------------------------------------------------------
# 2. POWER (b^e) USING RECURSION
# Question: recursion se b^e calculate karo
# -------------------------------------------------------------

def power(b, e):
    if e == 0:
        return 1
    else:
        return b * power(b, e - 1)

b = int(input("Enter base: "))
e = int(input("Enter exponent: "))
print(power(b, e))



# -------------------------------------------------------------
# 3. BINARY CONVERSION USING RECURSION
# Sample: input = 2 → output = 010
# -------------------------------------------------------------

def Bin(a):
    if a == 0:
        return 0
    else:
        return (a % 2) + 10 * Bin(a // 2)

a = int(input("Enter number for binary: "))
print("0", Bin(a), sep="")



# -------------------------------------------------------------
# 4. SUM OF DIGITS USING RECURSION
# Example: 4532 → 4+5+3+2 = 14
# -------------------------------------------------------------

def Sumof(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + Sumof(n // 10)

n = int(input("Enter number to find sum of digits: "))
print(Sumof(n))
