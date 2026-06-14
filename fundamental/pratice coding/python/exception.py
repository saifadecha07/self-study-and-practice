try:
    num1 = int(input("1 = "))
    num2 = int(input("2 = "))
    if num1<0 or num2<0:
        raise Exception("OH man our program must be positive number")
    result = num1/num2
    print(f"{result}")
except ValueError:
    print("Please genter enter only number")
except ZeroDivisionError:
    print("god bless you please do not divis by 0")
finally:
    print("--------------end program--------------")