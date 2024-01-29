import re

# data=re.findall("[0-9]","abcdef12gh45")
# print(data)

# data=re.findall("[^0-9]","abcdef12gh45")
# print(data)

# data=re.findall(".","abcdef12gh45")
# print(data)

# data=re.findall("[0-9]+","ab1cdef312gh45")
# print(data)

# data=re.findall("[0-9]*","abcdef12gh45")
# print(data)

# data=re.findall("[0-9]?","abcdef12gh45")
# print(data)

# data=re.findall("\d{2}","abc2def12gh45")
# print(data)

# data=re.findall("[0-9]{1,3}","ab1cd3211ef132gh45")
# print(data)

# data=re.findall("[+]91-[6-9][0-9]{9}","dsn2478534326sjfhd+91-87853261249vxcfd6785fbxb25")
# print(data)

# data=re.findall("[A-Z]{5}[0-9]{4}[A-Z]","AFN4FNJKR2365J23425DF")
# print(data)

# data=re.findall("AP[ ]?[0-3][1-9][ ]?[a-zA-Z][ ]?[0-9]{4}","AP08J9569T4")
# print(data)


# file=open(r"D:\Sravan_78\sravan_78\LICENSE.txt",'r')
# data=file.read()
# file.close()

# a=re.findall("[aeiouAEIOU]+",data)
# print(a)
# print(len(a))

# data=re.findall("[a-zA-Z][a-zA-Z0-9]+@gmail.com","453egvf857682753@gmail.comyugf")
# print(data)

# data=re.findall("[a-zA-Z0-9]+[.]?[a-zA-Z0-9]*@gmail.com","453egvf857682753@gmail.comyugf")
# print(data)

with open(r"C:\Users\administrator.MCA\Desktop\simple.txt.txt",'r+',encoding='utf-8') as file:
    data=file.read()
    a=re.sub("[ ]","_",data)
    file.seek(0)
    file.write(a)