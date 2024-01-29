a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=int(input("enter 3rd number: "))
if a>b and a>c :
      if b>c :
             print("b is 2nd greatest")
      else :
            print("c is 2nd greatest")
elif b>c :
      if c>a :
             print("c is 2nd greatest")
      else :
            print("a is 2nd greatest")
else :
      if a>b :
            print("a is 2nd greatest")
      else :
            print("b is 2nd greatest")