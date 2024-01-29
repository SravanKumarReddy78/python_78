def prime(num,i=2):
    if num>1:
        if num==i:
            return "prime number"
        elif num%i==0:
            return "Not a prime number"
        return prime(num,i+1)
print(prime(1))