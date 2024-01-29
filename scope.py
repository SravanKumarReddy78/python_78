a,b=10,20
def fun():
    c=20
    def inner():
        nonlocal c
        c=40
        print(a)
        print(c)
    print(c)
    inner()
    print(c)
fun()
