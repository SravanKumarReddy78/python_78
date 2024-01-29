s=[2,3,4,7,5]
d=[]
for b in s :
    fact=1
    for k in range(1,b+1) :
        fact*=k
    d+=[fact]
print(d)