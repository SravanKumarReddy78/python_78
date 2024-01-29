#k=[4,9,'abc',[1,2,3,4]]
#out={i:k[i] for i in range(len(k)) }
#out={i:j for i,j in enumerate(a)}
#print(out)

#a="abc"
#b=[1,2,3]
#out={a[i]:b[i] for i in range(len(a))}
#out={i:j for i,j in zip(a,b)}
#print(out)

a={'a':'abc',1:1234,'b':'bcde',2:2345}
#out={a[i]:i  for i in a if isinstance(a[i],str)}
out={a[i]:i  for i in a if type(a[i])==str}
print(out)