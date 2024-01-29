s="Hello my name is abhi"
i=0
d=""
while i<len(s) :
    if s[i]==' ':
        d+='_'
    else :
        d+=s[i]
    i+=1
print(d)