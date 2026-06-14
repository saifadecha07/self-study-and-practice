import math
def show():
    print("I love Agoda")
show()
def makeDream(x,y):
    print(f"{x} love {y}")
makeDream("i","you")
def makeDreamA(x="sky",y="agoda"):
    print(f"{x} love {y}")
makeDreamA(y="KBTG")
def makeDreamAgoda(*args): #tuple
    print(f"{args[0]} love {args[1]}")
makeDreamAgoda("x","s")
def agoda(**kwargs): #dictionary
    print(f"{kwargs['name']}")
agoda(name="sky",depart="engr")
def findArea(x,y):
    area = x**y
    return area
area = findArea(4,5)
print(f"{area}")
def getPI(x):
    a = x 
    return a*math.pi
print(getPI(5))
x = lambda l:l*5*510
print (x(5))