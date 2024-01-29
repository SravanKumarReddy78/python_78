print('choose ur destiny \n 1-->Chennai \n 2-->Delhi \n 3-->Mumbai \n 4-->Hydrabad')
destiny=input("select ur destiny: ")
print('Bus type \n 1-->AC \n 2-->Non-AC')
bus=int(input("select bus type: "))
adult=int(input("enter no.of adults: "))
child=int(input("enter no.of child: "))
acharge1=10
ccharge1=5
acharge2=5
ccharge2=3
if destiny=='1' :
    distance=350
    if bus==1 :
         print("total amt: ",(distance*adult*acharge1)+(distance*child*ccharge1))
    else :
         print("total amt: ",(distance*adult*acharge2)+(distance*child*ccharge2))
elif destiny=='2' :
    distance=2000
    if bus==1 :
         print("total amt: ",(distance*adult*acharge1)+(distance*child*ccharge1))
    else :
         print("total amt: ",(distance*adult*acharge2)+(distance*child*ccharge2))
elif destiny=='3' :
    distance=800
    if bus==1 :
         print("total amt: ",(distance*adult*acharge1)+(distance*child*ccharge1))
    else :
         print("total amt: ",(distance*adult*acharge2)+(distance*child*ccharge2))
elif destiny=='4' :
    distance=500
    if bus==1 :
        print("total amt: ",(distance*adult*acharge1)+(distance*child*ccharge1))
    else :
        print("total amt: ",(distance*adult*acharge2)+(distance*child*ccharge2))
else :
    print("select a valid destiny")