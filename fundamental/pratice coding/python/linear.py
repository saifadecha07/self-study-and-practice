import math

m1 = float(input("m1: "))
b1 = float(input("b1: "))
m2 = float(input("m2: "))
b2 = float(input("b2: "))
m3 = float(input("m3: "))
b3 = float(input("b3: "))
print(m1,b1,m2,b2,m3,b3)
x1 = (b2-b1) / (m1 - m2)
y1 = (m1*x1) + b1

x2 = (b3-b2) / (m2-m3)
y2 = (m2*x2) +b2

x3 = (b1 - b3) / (m3-m1)
y3 = (m3*x3) +b3

area = 0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
print(f"{area:.3f}")


s = float(input("enter sec"))
h = s//3600
m = (s//60-h*60)
print(h,m)


price = float(input("enter price "))
price1 = ((price-50)//100)*100+98
print(int(price1))

