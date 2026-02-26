#Default Function
"""def number():
    for i in range (1,6):
        print(i)
number()"""

# Parameterized Function
"""num1 = int(input("Enter the number :"))
num2 = int(input("Enter the number :"))
def number(num1,num2):
    a = num1 + num2
    print(a)
number(num1,num2)"""



num = int(input("Enter the number :"))
def number(num):
    if num%2 == 0:
        print("even number")
    elif num%2 == 1:
        print("Odd number")
    else :
        ("Invalid number try again!!!!")
number(num)

    