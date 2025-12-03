# write a program to reverse a four digit number using % and // operator
num = eval(input("ENTER NUMBER"))

a = num % 10          # 1st digit (last one)
b = (num // 10) % 10  # 2nd digit
c = (num // 100) % 10 # 3rd digit
d = num // 1000       # 4th digit

print(a, b, c, d)
