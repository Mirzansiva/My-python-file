x = [[10,20,30],[40,50,60],[70,80,90]]
print(x)
print(type(x))
print("x[0][1] :",x[0][1])
print("x[1][2] :",x[0][1])
a = 0
while a < len (x):
    j = 0
    while j < len (x[a]):
        print(x[a][j],end=" ")
        j += 1
    print()
    a+=1

