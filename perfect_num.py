num=int(input("enter a num: "))
sum=0
i=1
while i<=num/2 :
    if num%i==0 :
        sum+=i
    i+=1
if sum==num :
    print(num,"is a perfect number")
else :
    print(num,"is not a perfect number")