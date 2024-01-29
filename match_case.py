#num=input("entre a number from 0-6: ")
#match num:
#    case "0":
#        print("sunday")
#    case "1":
#        print("monday")
#    case "2":
#        print("tuesday")
#    case "3":
#        print("wednesday")
#    case "4":
#        print("thursday")
#    case "5":
#        print("friday")
#    case "6":
#        print("saturday")
#    case _:
#        print("enter a valid input")


#a=int(input("entre a number: "))
#b=int(input("entre a number: "))
#c=input("entre a arithmetic operator: ")
#match c:
#    case "+":
#        print(a+b)
#    case "-":
#        print(a-b)
#    case "*":
#        print(a*b)
#    case "**":
#        print(a**b)
#    case "/":
#        print(a/b)
#    case "//":
#        print(a//b)
#    case "%":
#        print(a%b)
#    case _:
#        print("enter a valid operator")


a=int(input("enter a num: "))
match a%2==0:
    case 0:
        print(a**2)
    case 1:
        print(a**3)
    case _:
        print("imvalid")
