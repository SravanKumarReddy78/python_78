def fact():
    a=int(input("enter a number: "))
    fact1=1
    for i in range(1,a+1) :
        fact1*=i
    print(fact1)
fact()