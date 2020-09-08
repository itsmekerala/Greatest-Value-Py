a=int(input("Enter the First value: "))
b=int(input("Enter the Second value: "))
c=int(input("Enter the Third value: "))
if a>b and a>c:
    print (a,"is the greatest Value")
elif b>a and b>c:
    print(b,"is the greatest  Value")
elif c>a and c>b:
    print (c,"is the greatest Value")
elif a==b:
    print (a, "and" ,b, "are Equal value's")
elif a==c:
    print (a, "and",c," are Equal value's")
elif b==c:
    print (b, "and" ,c," are Equal value's ")
elif b==a:
    print(b, "and" ,a, "are Equal value's")
else:
    print ("No Answer")
