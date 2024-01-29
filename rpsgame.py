print('enter \n 1-->Rock \n 2-->Paper \n 3-->Scissor')
p1=input("enter 1st input: ")
p2=input("enter 2nd input: ")
if p1=='1' and p2=='2' :
    print("p2 is winner")
elif p1=='2' and p2=='3' :
    print("p2 is winner")
elif p1=='3' and p2=='1'  :
     print("p2 is winner")
elif p1==p2 :
    print("match tie")
else :
    print("p1 is winner")