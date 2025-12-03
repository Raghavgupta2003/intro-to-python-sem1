# -------------------------------------------------------------------
# 1. Print numbers except multiples of 5
# -------------------------------------------------------------------
a = int(input("Enter number: "))
for i in range(1, a + 1):
    if i % 5 == 0:
        continue
    print(i, end=" ")
print("\n")


# -------------------------------------------------------------------
# 2. Star pattern increasing & decreasing
# -------------------------------------------------------------------
n = int(input("Enter n for star pattern: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
print()


# -------------------------------------------------------------------
# 3. Multiplication table (n x n)
# -------------------------------------------------------------------
n = int(input("Enter n for multiplication table: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()
print()


# -------------------------------------------------------------------
# 4. Number pattern increasing & decreasing
# -------------------------------------------------------------------
n = int(input("Enter n for number pattern: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()


# -------------------------------------------------------------------
# 5. Find month name
# -------------------------------------------------------------------
a = int(input("Enter month number: "))
months = [
    "Invalid", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

if 1 <= a <= 12:
    print(months[a])
else:
    print("Invalid")
print()


# -------------------------------------------------------------------
# 6. Find number of days in a month
# -------------------------------------------------------------------
a = int(input("Enter month number for days: "))
if a in (1, 3, 5, 7, 8, 10, 12):
    print("31 days")
elif a == 2:
    print("28 or 29 days")
elif a in (4, 6, 9, 11):
    print("30 days")
else:
    print("Invalid")
print()


# -------------------------------------------------------------------
# 7. Count digits in a number
# -------------------------------------------------------------------
a = input("Enter a number: ")
print("Number of digits:", len(a))
print()


# -------------------------------------------------------------------
# 8. Grade → student age mapping
# -------------------------------------------------------------------
g = int(input("Enter grade (1-5): "))
grades = {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}

if g in grades:
    print("Age:", grades[g])
else:
    print("Invalid")
print()


# -------------------------------------------------------------------
# 9. For loop demo
# -------------------------------------------------------------------
print("For-loop ranges:")
for i in range(-78, -65, 2):
    print(i)

for j in range(92, 120, 1):
    print(chr(j), end="")
print()

for k in range(65, 75, 2):
    print(k)
print()


# -------------------------------------------------------------------
# 10. Square of numbers
# -------------------------------------------------------------------
for i in range(1, 6):
    print("Square of", i, "=", i * i)
print()


# -------------------------------------------------------------------
# 11. Even numbers from 1–10 and sum
# -------------------------------------------------------------------
sum_even = 0
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
        sum_even += i
print("Sum =", sum_even)
print()


# -------------------------------------------------------------------
# 12. Print each character separated by comma
# -------------------------------------------------------------------
s = input("Enter string: ")
for i in s:
    print(i, end=",")
print("\n")


# -------------------------------------------------------------------
# 13. Multiply n by itself n times (n^n)
# -------------------------------------------------------------------
n = int(input("Enter number for n^n: "))
p = 1
for i in range(1, n + 1):
    p *= n
print("Result =", p)
