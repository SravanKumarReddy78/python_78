s=[1,'1',2,2.4,[4,5,6],9,16,"abcd"]
i=0
for k in s :
    if type(k)==int :
     if k%2==0 :
        i+=k
     else :
        i-=k
print(i)