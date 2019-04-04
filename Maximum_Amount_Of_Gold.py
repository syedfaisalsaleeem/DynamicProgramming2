#python3
import numpy as np
arr=[]
input1=[int(x) for x in input().split()]
W=input1[0]
#print(W)
value=input1[1]
cnput2=[int(x) for x in input().split()]
cnput2.insert(0,0)
#print(cnput2[0])
matrix = np.zeros(shape=(value+1,W+1), dtype=int)

for u in range (value+1):
    arr.append(1)
#print(arr)
##for y in range (value+1):
##    matrix[y,0]=y
##for x in range (W+1):
##    matrix[0,x]=x

#print(matrix)
##
for i in range (1 ,value+1):
    for w in range (1, W+1):
        matrix[i,w]=matrix[i-1,w]
        if cnput2[i]<=w:
            val=matrix[(i-1),(w-cnput2[i])]+cnput2[i]
            if matrix[i,w]<val:
                matrix[i,w]=val
#print(matrix)
print(matrix[-1,-1])
