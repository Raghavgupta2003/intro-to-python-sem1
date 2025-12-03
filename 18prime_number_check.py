# write a program to check the number is prime or not by using if and else

num = int(input('num: '))
flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print('not prime')
    else:
        print('num is prime')

else:
    print('not prime')
