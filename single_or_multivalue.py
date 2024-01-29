x=eval(input('enter value '))
if type(x) in [int,float,complex,bool]:
    print(x**2)
else :
    print(3*len(x)+1)