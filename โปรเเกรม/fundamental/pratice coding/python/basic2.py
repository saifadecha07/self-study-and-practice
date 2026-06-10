grade = float(input("enter your score "))
if 100 >= grade >= 80:
    print("A")
elif 79 >= grade >= 70:
    print("B")
elif 69 >= grade >= 0:
    print("F")
else:
    print("Invalid")
print("A") if grade >= 50 else print("F")