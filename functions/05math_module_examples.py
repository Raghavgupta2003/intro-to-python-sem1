# functions and math module in python:
# question
'''Take an edge a of the tetrahedron as an input from the user.
Write a python program to find the Surface area of the tetrahedron.
Formula :
Print the Area up to 2 decimal places.
1 <= a <= 103

a can be integer and as well a floating point value.



Sample Test case:

3 ----> Input edge a of a tetrahedron.

15.59 ----> Print the surface area of the tetrahedron.
'''
#solution
'''import math
def area_of_tetrahedral(a):
    return (math.sqrt(3))*a*a
a=int(input())
print("%.2f"%area_of_tetrahedral(a))'''
#question
'''find cuberoot of 27'''
#solution
'''import math
x=int(math.cbrt(27))
print(x)'''
#question
'''our task is to:

Take an edge a of the Octahedron as an input from the user.
Write a python program to find the Volume of the octahedron.
Formula :

Print the Volume up to 2 decimal places.

12:27 PM


3 ----> Input edge a of a Octahedron.'''
#solution
'''import math
def area(a):
    
    x=((math.sqrt(2))*a**3)/3
    return x
a=int(input())
print("%.2f"%area(a))'''
# question
'''Write a simple program that reads an angle value in degrees(integer or floating point value) from the user.and prints the sine value of the given angle.
To find the sine value, firstly the given angle in degrees should be converted to radians.
print the result up to 2 decimal places.


Constraints:

1 <= integer <= 360.
Make use of mathematical functions defined in math module.
Sample test case:

30

0.50'''
# solution
'''import math
def sine(a):
    return math.sin(math.radians(a))
a=int(input())
print("%.2f"%sine(a))'''
# question
# strong number: 1!+ 4!+ 5! =145
'''Take an integer as input from the user.
Write a program to print all the strong numbers till the given integer n .


Strong number:

Strong number is a special number whose sum of the factorial of digits is equal to the original number.

For Example: 145 is strong number. Since, 1! + 4! + 5! = 145.



Hint: Use the concept of function composition and math module to achieve the result

500

1 2 145 ---->Output is printed space separated'''
#solution
'''import math

num = int(input())
def strong(num):

    for N in range(1, num):
        temp = N
        sums = 0
        while(temp > 0):
            rem = temp % 10
            fact = math.factorial(rem)
            sums = sums + fact
            temp = temp // 10

        if (sums == N):
            print("%d " %N,end="")

strong(num)'''
# question
'''A bugged code is given to you may have Syntax error or logical error. Your task is to rectify them and execute the test cases successfully.'''
#solution
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n%x ==0):
                return False
            else:
                return True
n=eval(input())
print(test_prime(n))





                                        
        
        
        



































































