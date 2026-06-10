start = int(input("start "))
stop = int(input("stop "))

for i in range (start,stop+1):
    for j in range(1,13):
        print((i),"x",(j)," ",(i*j))
