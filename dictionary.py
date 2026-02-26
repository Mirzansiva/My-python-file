"""data = {
    "name":"Mirzan",
    "age":18,
    "gender":"Male"
    }
    
print(data)
print(type(data))"""

d = [("name","Mirzan"),("age",18),("gender","Male")]
data = dict(d)
print(data)
print(type(data))
print(data["name"])
print(data["age"])
print(data["gender"])
print(data.get("name")) 
print(data.get("city")) 
"""print(data["city"])"""  



data["NIC"] = 198742047807
print(data)
data.update({"age":40,"NIC":198872})
print(data)

del data["name"]
print(data)
data.pop("age")
print(data)
data.popitem()
print(data)
data.clear()
print(data)