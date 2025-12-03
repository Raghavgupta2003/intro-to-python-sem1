#fabonaaccci
n=int(input())
n1=0
n2=1
nextterm=0
l=[]
for i in range (0,n):
        #l.append(nextterm)
        l+=[nextterm]
        n1=n2
        n2=nextterm
        nextterm=n1+n2
print(tuple(l))
        
#fabonaacci
n=int(input())
n1=0
n2=1
i=0
while(i<=n):
    print(i)
    n1=n2
    n2=i
    i=n1+n2

#fabonaacci and sum of even numbers
n=int(input())
n1=0
n2=1
i=0
sum=0
even=0
while(i<=n):
    print(i)
    if sum%2==0:
        even+=i
    n1=n2
    n2=i
    i=n1+n2
    sum+=1
print("sum of even terms are",even)

    
