d=int(input("enter a number: "))
count=0
i=2
while i<=d/2 :
    if d%i==0 :
      count+=1
    i+=1
if count==0 :
    print("prime")
else :
    print("not a prime")