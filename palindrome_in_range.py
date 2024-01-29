d=[]
for k in range(100,1000) :
    if str(k)==str(k)[: :-1]:
        d+=[k]
print(d)