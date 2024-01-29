a=int(input("enter a num: "))
for i in range (1,a+1):
    for j in range(1,a+1):
        if i==(a//2)+1 or j==(a//2)+1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print(" ")

    