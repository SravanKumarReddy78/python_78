import random
c=[]
while len(c)<6:
    c+=[random.choice(['@','#','$','*','!','&','?'])]
    c+=[chr(random.randint(97,122))]
    c+=[str(random.randint(0,9))]
random.shuffle(c)
captcha=""
for i in c:
    captcha+=i
print(captcha)