num1 = int(input("Enter the number :"))
num2 = int(input("Enter the number :"))
selection = input("Enter the selection :")
if selection == "addition":
    add = num1 + num2
    print(num1,"+",num2,"=",add)
elif selection == "subsraction":
    sub = num1 - num2
    print(num1,"-",num2,"=",sub)
elif selection == "multiplication":
    mul = num1*num2
    print(num1,"*",num2,"=",mul)
elif selection == "division":
    div = num1 / num2
    print(num1,"/",num2,"=",div)
else :
    print("Invalid number")

