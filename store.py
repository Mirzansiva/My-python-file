## basic foundtion for beginner
name = "Mirzan"
print (name)
print(type (name))

#################################################################################################
id = 20250169
name = "Mirzan"
age = 18
print ("My id is :"+str(id),"\nMy name is :",name,"\nmy age is :"+str(age))

###############new model Formate##############################################################
id = 20250169
name = "Mirzan"
age = 18
output = f"my name is {name}\nMy id is {id}\nMy age is {age}"
print(output)

##################old model format###############################################################################
id = 20250169
name = "Mirzan"
age = 18
output = "my name is {0}\nMy id is {1}\nMy age is {2}".format(id,name,age)
print(output)


###############################################################################################
id = 20250169
name = "Mirzan"
age = 18
output = "my name is {0}\nMy id is {1}\nMy age is {2}".format(id,name,age)
print("My name is %s \nMy id is %d \nMy age is %d"%(name,id,age));

