class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

class B(A):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d

class C(B):
    def __init__(self,a,b,c,d,g,h):
        super().__init__(a,b,c,d)
        self.g=g
        self.h=h

class D(A):
    def __init__(self,a,b,e,f):
        super().__init__(a,b)
        self.e=e
        self.f=f
        
mds=C(4,5,6,7,8,9)
skr=D(2,3,1,0)
