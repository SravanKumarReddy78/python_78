def a(li):
    i=0
    while i<len(li):
        if i%2==0 :
            if li[i]%2==0:
                li[i]=(i**2)+(li[i]**2)
            else:
                li[i]=i+li[i]
        else :
             if li[i]%2==0:
                li[i]=i+li[i]
             else:
                li[i]=(i**2)+(li[i]**2)
        i+=1
    return li
print(a([2,4,9,7,11,2,4,3,5,7,6]))
