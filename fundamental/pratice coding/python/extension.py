A=[i+1 for i in range(1,10+1) if i %2==0]
#list comprehesion
B=[[i,j,k] for i in range(1,3) for j in range(1,2) for k in range(1,3) if i+j+k != 2]
print(A+B)