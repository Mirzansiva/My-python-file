num1 = int(input("Enter the number :"))
num2 = int(input("Enter the number :"))
operator = input("Enter your operator sympol :")

match operator:

    case "+":
        def addition(num1 , num2):
            return num1 + num2
        add = addition(num1 , num2)
        print (add)
    
    case "-":
        def substraction (num1 , num2):
            return num1 - num2
        sub = substraction(num1, num2)
        print(sub)

    case "*":
        def multipliction(num1,num2):
            return num1*num2
        mul = multipliction (num1,num2)
        print(mul)
        
    case "/":
        def division (num1 , num2):
            return num1/num2
        div = division(num1,num2)
        print(div)
        
    case _:
        print("Ivalid sympoll")
        
    
