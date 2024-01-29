def sum_of_even(num):
    sum=0
    d=0
    if len(str(num))==6:
        while num>0:
            d=num%10
            num//=10
            if d%2==0:
                sum+=d
        return(sum)
    else:
        print("enter 6 digit number")
print(sum_of_even(789014))
