def mds(skr):
    temp=''
    for i in skr:
        if i in "aeiouAEIOU":
            temp+=i
    j=-1
    out=''
    for k in skr:
        if k in "aeiouAEIOU":
            out+=temp[j]
            j+=-1
        else:
            out+=k
    return out
print(mds('dia'))