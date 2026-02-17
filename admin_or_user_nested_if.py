username = input("Enter your username :")
Password = input("Enter your password :")
role = str(input("Enter your role :"))
if username == "Yarl It" and Password == "1234yit":
    if role == "admin":
        print("welcome admin")
    elif role == "user" :
        print("welcome user")
    else :
        print("This can't consider as a role; put the correct term")
else :
    print("your username or password is wrong; input correct term!!!!!!")