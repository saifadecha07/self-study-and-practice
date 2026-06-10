import math
print("This Program calculate 3 input for are of triangle")
a = float(input(""))
b = float(input(""))
c = float(input(""))
cr = c*math.pi/180
area = (1.0/2)*a*b*math.sin(cr)
print("area = ",area,"(sq cm)")