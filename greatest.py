a=int(input("enter 1st Number: "))
b=int(input("enter 2st Number: "))
c=int(input("enter 3st Number: "))
if (a>b)and (a>c):
    print (a,"is the greatest")
elif (b>a)and(b>c):
    print (b,"is the greatest")
elif (a==b):
    print("1st and 2nd Numbers are same")
elif(a==c):
    print("1st and 3nd Numbers are same")
else:
    print(c,"is the greatest")
