"""s = {"Maths","Science","Ict","Maths","Science"}
print(s)
print(type(s))
print(len(s))
s.add("tamil")
print(s)

### unodered
### unchangeable
### dublicate not allowed


s.update(["Physicss","Chemistry","Biology"])
print(s)
#s.add([   ])
#print(s)this is shows error

s.remove("Ict")
print(s)
s.discard('Ict')
print(s)

#s.remove("english")
#print(s)
#s.discard("english")
#print(s)
s.pop()
print(s)
my_sub = ["Tamil","English"]
s.update(my_sub)
print(s)"""



"""a = {1,2,3,4,5,}
b = {3,5,6,8,9,7}
c = a.union(b) 
# c = a/b
print(c)
d = a - b 
print(d)
e = b - c
print(e)

f = a.symmetric_difference(b)
print(f)"""

a = {1,2,3}
b = {1,2,3,4,5}
c = {4,5,6}
d = a|b|c
print(d)
e = a&b&c
print(e)
print(a>=b)
print(b.issuperset(a))
print(a.issuperset(b))
print(b>=a)
