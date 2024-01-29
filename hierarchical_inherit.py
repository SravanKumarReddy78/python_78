class A:
    def __init__(self,c,d):
        self.c=c
        self.d=d

class B(A):
    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f

class C(A):
    b=40

    def __init__(self,c,d,g,h):
        super().__init__(c,d)
        self.g=g
        self.h=h
        
mds=C(4,5,6,7)
skr=B(2,3,1,8)

