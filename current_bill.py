unit=int(input("Enter your unit: "))
if(unit>=0 and unit<=90):
    amount=unit*7
elif(unit>90 and unit<=150):
    remain=unit-90
    amount=(90*7)+(remain*10)
elif(unit>150 and unit<=300):
    remain1=unit-210
    m1=remain1*7
    remain2=unit - 
    amount = (90*7)+(remain2*10)+remain3*15
    print(amount)
else:
    print("wrong")
    