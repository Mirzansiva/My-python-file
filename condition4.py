tax = 0
net_salary = 0
name = str(input("Enter empoyee name :"))
salary = int(input("Enter the salary :"))
if salary  >= 100000:
    tax = salary*5/100
    net_salary = salary - tax
    print(net_salary)
elif salary <100000 and salary >= 80000:
    tax = salary*3/100
    net_salary = salary - tax
    print(net_salary)
else:
    print("no tax")
    
    