s=input("enter a string: ")
i=0
d=[]
start=0
while i<len(s) :
      if s[i]==" " :
        d+=[s[start:i]]
        start=i+1
      i+=1
if start<i :
    d+=[s[start:]]
print(d)