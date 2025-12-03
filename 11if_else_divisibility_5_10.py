n = int(input("enter the number: "))

if n % 5 == 0 and n % 10 == 0:
    print("n is divisible by both 5 and 10")
elif n % 5 == 0 or n % 10 == 0:
    print("n is divisible by either 5 or 10")
else:
    print("n is not divisible by 5 or 10")
    
    
