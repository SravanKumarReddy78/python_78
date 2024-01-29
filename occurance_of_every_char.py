s=input("enter a string: ")
d={}
for char in s :
    if not char in d :
        d[char]=1
    else :
        d[char]+=1
print(d)