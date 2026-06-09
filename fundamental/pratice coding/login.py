username = input("enter Username")
password = input("enter your pass")

if password =="123" and username == "admin" :
    print("log in")
if password =="123" or username == "admin" :
    print("log in")
if username != "admin" :
    print("can't log in")
else:
    print("failed")