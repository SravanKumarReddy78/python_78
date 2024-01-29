def mds(arr):
    skr=[]
    for i in arr:
        if type(i) in[str,list,tuple,set,dict]:
            for j in i:
                skr+=[j]
    return skr
print(mds(['abcd',[1,2,3]]))