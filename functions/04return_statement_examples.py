# return statement in function
#(it will exit from function and allocate to function caller)
'''def sum(a,b):
    return(a+b)
print(sum(10,20))'''
# we can also write this by using
'''def sum(a,b):
    c=a+b
    print(c)
sum(10,20)'''
# call by reference / value
'''def sum(a):
    a[0]="hello"
list1=[10,20,30,50]
sum(list1)
print(list1)'''
# example of same with 2 ways
# method 2
'''def sum(a):
    a+=10
    print(a)
b=30
sum(b)
print(b)'''
# method 1
'''def sum(x,y):
    z=x+y
    return z
print(sum(10,20))'''
######################################     anonmyous function in python  they work in single line   #####################################
# e.g. cube , lambda ,zip ,map....    (# cube is used with def)
# use of lambda :
'''a=lambda x,y,z: x+y+z
print(a(10,20,30))'''
# use of lamda:
'''cube=lambda a: a*a*a
print(cube(3))'''
#function with in function:
def sum(x,y):
    mul(x,y)
    print(10,20)
    mul(10,20)


def mul(a, b):
    print(a * b)

sum(5, 6)






