'''program to perform diff arithmetic operations
    1=Addition
    2=Substraction
    3=Multplication
    4=divison
'''

# Arithmetic operations menu
num1=int(input('num1: '))
num2=int(input('num2: '))
choice=int(input('choice: '))
if choice==1:
    print('addition',num1+num2)
elif choice==2:
    print('substraction',num1-num2)
elif choice==3:
    print('multiplication',num1*num2)
elif choice==4:
    print('divison',num1/num2)
else:
    print('invalid syntax')


        
