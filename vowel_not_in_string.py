def filter(string):
    d="aeiouAEIOU"
    s=''
    for i in d:
        if i not in string:
            s+=i
    return s
print(filter("srAvankUmarreddy"))