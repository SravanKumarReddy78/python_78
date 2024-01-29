s=input("enter a string: ")
d=""
i=0
while i<len(s) :
    if 'a'<=s[i]<='z' :
        d+=chr(ord(s[i])-32)
    else :
        d+=s[i]
    i+=1
print(d)