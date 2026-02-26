"""student = ("Mirzan",18,"2008/10/23")
fname,age,dof = student #in here we put only got 3 so we can put only 3 ecpected one 
print(fname)
print(age)
print(dof)"""  


marks = (75, 80,62,38,47,96)
a,*b,c = marks
print(a)
print(b)
print(c)

a,b,*c = marks
print(a)
print(b)
print(c)

*a,b,c = marks
print(a)
print(b)
print(c)



