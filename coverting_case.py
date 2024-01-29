def toggle():
    s=input("enter a string: ")
    d=""
    for i in s:
        if 'a'<=i<='z' :
            d+=chr(ord(i)-32)
        elif 'A'<=i<='Z' :
            d+=chr(ord(i)+32)
        else :
            d+=i
    return(d)
y=toggle()
print(y)