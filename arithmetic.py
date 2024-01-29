a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=input("enter arithmetic operator: ")
if c=='+' :
    print(a+b)
elif c=='-' :
    print(a-b)
elif c=='*' :
    print(a*b)
elif c=='**' :
    print(a**b)
elif c=='/' :
    print(a/b)
elif c=='//' :
    print(a//b)
elif c=='%' :
    print(a%b)
else :
    print("enter arithmetic operator")