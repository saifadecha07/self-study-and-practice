username = input("enter Username")
password = input("enter your pass")
if password =="1234" and username == "member" :
    print("log in")
    trans = int(input("enter your need"))
    if trans == 1:
        print("draw")
    elif trans == 2:
        print("Increase")
    else:
        print("Invalid")
else:
    print("don't know who you are")