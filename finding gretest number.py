a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if(a>b and a>c):
    print("greatest number is:",a)
elif(b>a and b>c):
    print("greatest number is:",b)
elif(c>a and c>b):
    print("greatest number is:",c)
else:
    print("entered two or more numbers are same")


