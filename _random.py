import random
number=random.randint(100,1000)
while True:
    a=int(input("a: "))
    if a==number :
        print("congrats u successfully guess correct num",a)
        break
    elif a<number :
        print("enter some greater number")
    else :
        print("enter some lesser number")