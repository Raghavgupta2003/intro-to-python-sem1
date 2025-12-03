#basics
'''
name = "Tony Stark"
age = 51
is_genius = True
print(name)
print(age)
print(is_genius)
'''
#user input
'''
name = input("what is your name?")
print("hello "+name)

tony = input("what is your superhero name : ")
print("it is "+tony)
'''
#type conversions
'''
old_age = input("Enter your old age : ")
new_age = int(old_age) + 2
print(new_age)


number = 18
print(float(18))

# Sum program
first = input("enter the first number: ")
second = input("enter the second number: ")

sum = int(first) + int(second)
print(sum)
print("The sum is: " + str(sum))
'''

#Strings
'''
name = "Tony Stark"

# string upper
new_name = name.upper()
print(new_name)
#string lower
lo = name.lower()
print(lo)
# string find fxn
x = name.find('S')
print("S is at index: "+ str(x))

x = name.find('Stark')
print("Stark is at index: "+ str(x))
#string replace
new_name = name.replace("Tony", "Raj");
print(new_name)

# string "in"
x = 'rk' in name
print(x)
'''

#OPERATORS
'''
# Arithmetic operations
print(2+2)
print(2-3)
print(5*2)
print(5/2)
print(5//2)
print(5%2)
print(5**2)


# operator precedence
# (parenthesis) > (**) > (*, /, //, %) > (+, -)

#comparison operators
print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(3 <= 2)
print(3 == 3)
print(3 != 3)

#logical operators
print((3>2) or (3>4));
print((3>2) and (4>3));
print(not 4 < 5)
print(not 4)
'''

# if elif else
'''
age = 2
if(age >= 18):
    print("you are an adult")
    print("you can vote")
elif age<18 and age>3:
    print("you are in school")
else:
    print("you are a child")
print("thank you")

'''

#mini calculator
'''
first = input("enter first number : ")
op = input("enter operator(+, -, *, /, %) : ")
second = input("enter second number : ")

first = int(first)
second = int(second)

if op == '+':
    print(first + second)
elif op == '-':
    print(first - second)
elif op == '*':
    print(first * second)
elif op == '/':
    print(first/second)
elif op == '%':
    print(first % second)
else:
    print("INVALID OPERATION")
'''

# RANGE
'''
numbers = range(5)
print(numbers)

numbers = range(5,10)
print(numbers)

numbers = range(5, 100, 20)
print(numbers)
'''

#loop
'''

i = 1
while i<=8:
    print(i)
    i += 1

#pattern

i = 1
while i<=5:
    print(i * '*')
    i += 1

#reverse pattern

i=5
while(i >= 0):
    print(i * '*')
    i -= 1

#for loop

for item in range(5):
    print(item + 1)


for item in range(10, 15):
    print(item + 1)


for item in range(1, 20, 2):
    print(item + 1)
'''

# list
'''
marks = [95, 98, 97, "rajesh", "ramm"]
print(marks)
print(marks[0])
print(marks[-1])

# sublist
subMarks = marks[0:2];
print(subMarks)

# insert at end(append)
marks.append(22)
print(marks)

# insert at particular position
marks.insert(2, "ram");
print(marks)

# length
n = len(marks)
print(n)

#while loop on list
i=0
while i < len(marks):
    print(marks[i])
    i += 1

# emptying (clear()) the list
marks.clear()
print(marks)

# break and continue
students = ["ram", "shyam", "kishan", "radha", "radhika"]

for stu in students:
    if(stu == "radha"):
        break #break the loop
    print(stu)


for stu in students:
    if(stu == "kishan"):
        continue;  #skip kishan
    print(stu)
'''

# TUPLE: similar to list but immutable
# small parenthis used
'''
marks = (99, 89, 45, 97, 97, 89, 97)
print(marks)
stu = "ram", "shyam", "raj"
print(stu)

#marks[0] = 55 #error since tuples are immutable

# freq of a ele in tuple 
print("freq of 97 : "+ str(marks.count(97)))
print("freq of 89 : "+ str(marks.count(89)))
print("freq of 45 : "+ str(marks.count(45)))

# index of ele in tuple
print("index of 97 : "+str(marks.index(97)))
'''
#SETS
#index not exist in set
# curly breackets {}
# unique values
'''
marks = {95, 98, 97, 97, 97}
print(marks) # only unique values printed

for score in marks:
    print(score)
'''

# DICTIONARY
# key:value pairs are stored
'''
marks = {"english":95, "chemistry":98, "maths":95}
print(marks["chemistry"])

# adding new key pair
marks["physics"] = 99
print(marks)

#chnaging existing marks in dictionary
marks["chemistry"] = 55
print(marks)

# loop on dictionary
for subject in marks:
    print(str(subject)+ " : "+str(marks[subject]))

for sub in marks.keys():
    print(sub)

for mark in marks.values():
    print(mark)
'''

#FUNCTIONS
# 1) In-Build Functions
# 2) Module Functions
# 3) User Defined Functions

#Module Functions
import math
print(dir(math)) # this will print all the functions of maths


from math import sqrt
# from math import *
print(sqrt(4))


#user defined functions
def print_sum(first, second):
    print(first + second)

print_sum(1,2)


def print_SUM(first, second=4):
    print(first + second)

print_SUM(1,2)
print_SUM(1)




    






