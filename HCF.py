a,b=12,18
hcf=1
i=1
while i<=a and i<=b :
    if a%i==0 and b%i==0 :
        hcf=i
    i+=1
print(hcf)