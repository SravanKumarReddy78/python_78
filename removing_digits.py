s="user@123#admin"
i=''
for k in s:
    if '0'<=k<='9' :
        i+=''
    else :
        i+=k
print(i)