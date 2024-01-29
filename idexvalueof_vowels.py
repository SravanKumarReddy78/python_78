s=input("enter a string: ")
i=0
d=[]
for i in range(len(s)) :
    if s[i] in "aeiouAEIOU" :
        d+=[i]
    i+=1
print(d)