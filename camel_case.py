s="Hello my name is abhi"
i=0
d=""
temp=True
while i<len(s) :
    if s[i]==' ':
        temp=True
    elif temp and 'a'<=s[i]<='z' :
        d+=chr(ord(s[i])-32)
        temp=False
    else :
        d+=s[i]
        temp=False
    i+=1
print(d)