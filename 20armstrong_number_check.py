# armstrong number
n=str(input())
order=len(n)
y=0
for i in n :
    y+=(int(i))**order
if y==int(n):
    print("armstrong")
else:

    print("not an armstrong number")
