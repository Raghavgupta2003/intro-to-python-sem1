print(format(10.3456, "10.2f"))
# The above code prints the float number 10.3456 formatted to occupy a width of 10 characters with 2 digits after the decimal point.

a=eval(input("enter value:"))
print(format(a,".2f")) #formats to 2 decimal places
print(format(a,"10.3f")) #total width 10 with 3 decimal places
print(format(a,"10.2%")) #percentage format with 2 decimal places


print(format(20,"10x"))  #hexadecimal format
print(format(20,"10o"))  #octal format
print(format(20,"10b"))  #binary format


print(format("hello python",">25s")) #right align in width of 25


print(ord("A")) # ord is used to get ASCII value of character
print(ord("a"))


print(chr(90)) # chr is used to get character from ASCII value
print(ord('+'))
print(chr(45))

'''
input=weight of object in grams:2500
output=weight of object in kg and grams
'''
W1=eval(input("ENTER WEIGHT"))
print(W1)
W2=W1//1000#CALCULATE KG
print(W2)
W3=W1%1000#CALCULATE GRAMS
print(W2,W3)