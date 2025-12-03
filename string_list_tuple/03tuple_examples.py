# ------------------------------------------------------------
# 1. Convert tuple → list → modify → list → tuple
# ------------------------------------------------------------
mytuple = ("i", "love", "python")
print("Given Tuple:", mytuple)

mylist = list(mytuple)
print("After Converting Tuple into List:", mylist)

mylist[1] = "practice"
print("List after changing element:", mylist)

finaltuple = tuple(mylist)
print("After Converting List into Tuple:", finaltuple)



# ------------------------------------------------------------
# 2. Tuple operations
# ------------------------------------------------------------
a = (20, 40, 60, "apple", "ball")
print(a)

t1 = (1,)
print(t1)

print(a[0])
print(a[2])
print(a[1:3])

b = (2, 3)
print(a + b)
print(b * 2)

a = (2, 3, 4, 5, 6, 7, 8, 9, 10)
print(5 in a)
print(100 in a)
print(2 not in a)

a = (2, 3, 4, 5, 6, 7, 8, 9, 10)
b = (2, 3, 4)
print(a == b)
print(a != b)



# ------------------------------------------------------------
# 3. Convert list input → tuple & print element using index
# Flexible input: comma OR space
# ------------------------------------------------------------
data = input("list: ")

# Auto-detect separator
if "," in data:
    list1 = data.split(",")
else:
    list1 = data.split()

print("list:", list1)

tuple1 = tuple(list1)
print("tuple:", tuple1)

index = int(input("index: "))

if index < len(tuple1) and index >= -len(tuple1):
    print("element:", tuple1[index])
else:
    print("enter valid syntax")



# ------------------------------------------------------------
# 4. Remove element at given index from tuple
# Flexible: comma OR space input
# ------------------------------------------------------------
data = input("data: ")

if "," in data:
    list1 = data.split(",")
else:
    list1 = data.split()

tuple1 = tuple(list1)
print("tuple:", tuple1)

index = int(input("index: "))
size = len(tuple1)

if index != -1:
    if index < size and index >= -size:
        tuple2 = tuple1[:index] + tuple1[index + 1:]
        print("after removing:", tuple2)
    else:
        print("enter valid index")
else:
    print("after removing:", tuple1[:index])
