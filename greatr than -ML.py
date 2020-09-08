a=int(input("ഒന്നാമത്തെ മൂല്യം നല്‍കുക  : "))
b=int(input("രണ്ടാമത്തെ മൂല്യം നല്‍കുക : "))
c=int(input("മൂന്നാമത്തെ മുല്യം നല്‍കുക : "))
if a>b and a>c:
    print (a,"ആണ് ഏറ്റവും ഉയര്‍ന്ന മൂല്യം ")
elif b>a and b>c:
    print(b,"ആണ് ഏറ്റവും ഉയര്‍ന്ന മൂല്യം")
elif c>a and c>b:
    print (c,"ആണ് ഏറ്റവും ഉയര്‍ന്ന മൂല്യം")
elif a==b:
    print (a,",",b, "ഒരേമൂല്യം ആണ് ")
elif a==c:
    print (a,",",c," ഒരേമൂല്യം ആണ് ")
elif b==c:
    print (b,",",c," ഒരേമൂല്യം ആണ്  ")
elif b==a:
    print(b,",",a, "ഒരേമൂല്യം ആണ് ")
else:
    print ("തരകാലം ഉത്തരമില്ല ")
