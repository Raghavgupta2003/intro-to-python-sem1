#global and local variable
#local: we have to print result inside the function
'''def sum():
    s="sum of statement"
    print(s)
sum()'''
# there are two ways to initalize global variable

#method 1
'''def sum():
    print("hi python")
s="outside function"
sum()
print(s)'''
# method 2
'''def sum():
    global s
    s="outside the function"
sum()
print(s)'''
# question
'''First, create a global variable x and initialise it to 20.
Now, create a Add() function with a combination of local variables and global variables.
Create a local variable y and initialise it by taking input from the user.
print local variable and global variable as shown in the test case.
In the end, add a global variable x and local variable y to calculate the sum of two variables.
Call the Add() function and print the result.


Constraint:

Integer value of y can be a positive or negative integer.

Sample test case:

y: 30 ---> Input by the user

30 ----> local variable printed.

20 ----> global variable printed.

x+y: 50 ----> Result printed.'''
# solution

'''def add():
    y=int(input("y: "))
    print(y)
    global x
    x=20
    print(x)
    print("x+y:",x+y)
add()'''
# question
'''Complete two functions cube() and triple(). cube function will take integer value as input parameter and find the cube of the given value, and triple function will triple the value passed as parameter and both functions return the resultant value after doing their respective computations.
Your output 1 by using above listed functions is to triple the cube value of an integer n taken as input from the user.
Your output 2 by using above listed functions is to find the cube of the triple value of an integer n taken as input from the user.
Note: Call the functions using correct function composition to achive the resultant output.



Constraint:

Integer n taken as input can be a positive or negative integer.





Hint: Function composition of two functions looks like abc(def(ghi())), where one function is called and resultant value is passed as argument to another function..

Sample test case:

3 ----> Integer value input by the user

81 ----> Output 1

729 -----> Output 2

Editorial:

Output 1: 3 is integer input from the user, At first step cube of 3 is 27 and then when we triple the resultant value (27*3 = 81).

Output 2: 3 is integer input from the user, At first step triple the value 3-->(3*3 = 9)and then when we find the cube of the resultant value 9 it is 729.'''
# solution
a=int(input())
def cube():
    x=a*a*a
    z=3*x
    return z
print(cube())
def triple():
    y=a*3
    b=y**3
    print(b)
triple()























