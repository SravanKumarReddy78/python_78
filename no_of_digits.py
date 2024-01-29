def no_of_digits():
    a=int(input("enter a number: "))
    c=0
    while a>0:
        a=a//10
        c+=1
    print(c)
no_of_digits()