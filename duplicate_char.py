s="sravankumarreddy"
d=''
for i in range(len(s)) :
    if i!=len(s) and s[i] in s[i+1:] :
       d+=s[i]
print(list(d))
