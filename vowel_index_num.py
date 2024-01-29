def vowel_index(string):
    s=[]
    i=0
    while i<len(string):
        if string[i] in "aeiouAEIOU":
            s+=[i]
        i+=1
    return(s)
print(vowel_index("sravan"))