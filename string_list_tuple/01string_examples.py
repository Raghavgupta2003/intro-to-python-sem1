# ------------------------------------------------------------
# STRING METHODS & BASIC OPERATIONS
# ------------------------------------------------------------

# uppercase, lowercase, replace, strip
H = " Python prograMMing  "
print(H.upper())
print(H.lower())
print(H.replace("Python", "java"))
print(H.strip())
print(H.lstrip())
print(H.rstrip())


# ------------------------------------------------------------
# SPLIT METHOD
# ------------------------------------------------------------
H = "Python programming"
print(H.split(" "))


# ------------------------------------------------------------
# STRING CONCATENATION
# ------------------------------------------------------------
a = "hello"
b = "world"
c = a + b
d = a + " " + b
print(c)
print(d)


# ------------------------------------------------------------
# FORMAT PLACEHOLDER
# ------------------------------------------------------------
a = "My name is"
b = "{} RG"
print(b.format(a))


# ------------------------------------------------------------
# CHECK BINARY STRING (ONLY 0 AND 1)
# ------------------------------------------------------------
s = input("Enter binary candidate string: ")
x = set(s)
y = {'0', '1'}

if x == y or x == {'0'} or x == {'1'}:
    print("True")
else:
    print("False")


# ------------------------------------------------------------
# STRONG PASSWORD CHECKER
# Conditions:
# >=8 chars, [a-z], [A-Z], [0-9], one of _ @ $
# ------------------------------------------------------------
password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False
valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@$")

if len(password) >= 8:
    for ch in password:
        if ch not in valid_chars:
            has_special = False
            break
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
        if ch in "_@$":
            has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong Password")
else:
    print("Weak Password")


# ------------------------------------------------------------
# STRING METHODS DEMO
# ------------------------------------------------------------
a = "STRing methOds with methods!"
print(a.isalpha())
print(a.upper())
print(a.isupper())
print(a.lower())
print(a.islower())
print(a.isdigit())
print(a.endswith('!'))
print(a.find("m"))
print(a.rfind("m"))


# ------------------------------------------------------------
# JOIN METHOD
# ------------------------------------------------------------
a = "STRing methOds with methods"
b = list(a)
print("**".join(b))

b = a.split()
print("!*!*!".join(b))


# ------------------------------------------------------------
# PARTITION METHOD
# ------------------------------------------------------------
a = "welcome to python world raj"
print(a.partition("python"))


# ------------------------------------------------------------
# LIST OPERATIONS
# ------------------------------------------------------------
list1 = ['1', 'hello', '24h', 3]
print(list1)

list2 = [4, 5, 62, 567, 1, 2, 0, 8]
list2.sort()
print(list2)
