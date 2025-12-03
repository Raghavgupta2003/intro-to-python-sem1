# ------------------------------------------------------------
# 1. Update value at given index in a list
# ------------------------------------------------------------
data = input("data: ")
list1 = data.split(",")
print("before updation:", list1)

index = int(input("index: "))

if index < len(list1) and index >= -len(list1):
    value = input("element: ")
    list1[index] = value
    print("after updation:", list1)
else:
    print("invalid")


# ------------------------------------------------------------
# 2. Largest among first and last elements
# ------------------------------------------------------------
data = input("data: ")
list1 = data.split(",")
size = len(list1)

if list1[0] < list1[-1]:
    print("largest among first,last elements:", list1[-1])
else:
    print("largest among first,last elements:", list1[0])


# ------------------------------------------------------------
# 3. Cloning using slicing
# ------------------------------------------------------------
a = [1, 2, 3, 4, 5]
print("a =", a)
b = a[:]
print("b = a[:]")
print("b =", b)
print("a is b ? :", a is b)

# Cloning using list()
a = [1, 2, 3, 4, 5]
b = list(a)
print("\nb = list(a)")
print("b =", b)
print("a is b ? :", a is b)


# ------------------------------------------------------------
# 4. Check if both lists share first or last element
# ------------------------------------------------------------
data1 = input("data1: ")
list1 = data1.split(",")

data2 = input("data2: ")
list2 = data2.split(",")

print(list1)
print(list2)

if list1[0] == list2[0] or list1[-1] == list2[-1]:
    print("True")
else:
    print("False")


# ------------------------------------------------------------
# 5. Remove duplicates from list
# ------------------------------------------------------------
data = input("data: ")
list1 = data.split(",")
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

print(list1)
print("after removing duplicates:", list2)


# ------------------------------------------------------------
# 6. Convert two lists into dictionary-like string
# ------------------------------------------------------------
data1 = input("data1: ")
data2 = input("data2: ")

l1 = data1.split(",")
l2 = data2.split(",")

str1 = '{'

if len(l1) != len(l2):
    print("lists are different lengths")
else:
    for i in range(len(l1)):
        str1 = str1 + "'" + l1[i] + "'" + ":" + "'" + l2[i] + "'" + ","

    print(str1[:-1] + "}")
