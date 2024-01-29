a=int(input("enter a num: "))
for i in range (1,a+1):
    for j in range(1,a+1):
        if i==j or i==a-j+1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print(" ")