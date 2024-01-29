def mds(skr,skb):
    sum=0
    i=0
    if len(skr)==len(skb):
        while i<len(skr):
            if skr[i]!=skb[i]:
                sum+=1
            i+=1
    else:
        print("length of two strings are diferent")
    return sum
print(mds('strong','string'))
