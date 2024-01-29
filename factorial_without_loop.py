def fact(num,out=1):
    if num==1:
        return out
    out*=num
    return fact(num-1,out)
print(fact(6))
