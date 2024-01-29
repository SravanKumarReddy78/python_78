a,b=12,14
lcm=1
hcf=1
i=1
while i<=a and i<=b :
    if a%i==0 and b%i==0 :
        hcf=i
        lcm=a*b//hcf
    i+=1
print(lcm)