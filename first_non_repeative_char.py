s="good morning"
i=0
while i<len(s) :
    if s[i] not in s[i+1:] :
        print(s[i])
        break
    i+=1