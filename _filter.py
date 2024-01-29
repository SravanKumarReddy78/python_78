#a=[1,0,True,'','str',[1,2,3],78,0.0]
#out=[i for i in a if bool(i)]
#out=list(filter(bool,a))
#print(out)


#b=[2,57,8,6,4,3,23,2,1,21,35,8,9]
#def mul3(num):
#    if num%3==0:
#        return True
#  else:
#       return False
#print(list(filter(mul3,b)))
#out=[i for i in b if i%3==0]
#out=list(filter(lambda i:i%3==0,b))
#print(out)


#b=[2,57,8,6,4,3,23,2,1,21,35,8,9]
#out=list(map(lambda i:i**2,b))
#print(out)


#b=[2,57,8,6,4,3,23,2,1,21,35,8,9]
#a=list(filter(lambda i:i%2==0,b))
#print(list(map(lambda i:i**3,a)))
#print(list(map(lambda k:k**3,filter(lambda i:i%2==0,b))))


#def fun(i):
#    if type(i) in [int]:
#        return i
#    else:
#        return len(i)
#i=[1,2,[4,5,6],'xyz',(4,1,2,3)]
#print(list(map(fun,i)))


#from functools import reduce
#reduce
#b=[2,3,4,5]
#print(reduce(lambda x,y:x+y,map(lambda a:a**2,b)))


#def fun(a,b):
#    yield a+b
#    yield a*b
#print(list(fun(3,2)))


#def fun(n):
#    a,b=0,1
#    for i in range(n):
#        yield a
#       a,b=b,a+b
#print(list(fun(10)))


#def fun(n):
#    a=1
#    for i in range(n):
#        yield a
#        a*=2
#print(list(fun(10)))


#class MbNoError(Exception):
#    pass
#
#mbno=int(input("enter a mobile number: "))
#if len(str(mbno))==10:
#    print("mobile number is validated")
#else:
#    raise MbNoError(f'number shoud be 10 digits but {len(str(mbno))} were given')


