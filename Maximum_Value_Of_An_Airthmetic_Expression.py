#python3
import numpy as np
def MinandMax(i,j,ope,m1max,m1min):
    #print(m1max)
    #print(m1min)
    min1=1000000
    max1=-1000000
    for k in range (i,j):
        #print(k)
        
        if ope[k]==('+'):
            a=np.add(m1max[i,k],m1max[k+1,j])
            b=np.add(m1max[i,k],m1min[k+1,j])
            c=np.add(m1min[i,k],m1max[k+1,j])
            d=np.add(m1min[i,k],m1min[k+1,j])
        elif ope[k]==('-'):
            a=np.subtract(m1max[i,k],m1max[k+1,j])
            b=np.subtract(m1max[i,k],m1min[k+1,j])
            c=np.subtract(m1min[i,k],m1max[k+1,j])
            d=np.subtract(m1min[i,k],m1min[k+1,j])
        elif ope[k]==('*'):
            a=np.multiply(m1max[i,k],m1max[k+1,j])
            b=np.multiply(m1max[i,k],m1min[k+1,j])
            c=np.multiply(m1min[i,k],m1max[k+1,j])
            d=np.multiply(m1min[i,k],m1min[k+1,j])


        min1=min(min1,a,b,c,d)
        max1=max(max1,a,b,c,d)
    return(min1,max1)

ope=[]
input1=str(input())
l=len(input1)
digits=int((l+1)/2)
#print(digits)
m1max = np.zeros(shape=(digits+1,digits+1), dtype=int)
m1min = np.zeros(shape=(digits+1,digits+1), dtype=int)
l3=0
i=1
for x in range (0,l+1):
    if (x%2 ==0):
        m1max[i,i]=input1[x]
        m1min[i,i]=input1[x]
        i=i+1
ope.append(0)
for x in range (0,l):
    if (x%2 !=0):
        l3=input1[x]
        ope.append(l3)
        
   
        
#print(ope)
##
##if ope[0]==('+'):
##    m1max[0,1]=np.add(m1max[0,0],m1max[1,1])
##m1max[0,1]=(m1max[0,0]) (ope[0])  (m1max[1,1])
##


##
##        a=m1max[k,i]
for s in range (1,digits):
    for i in range (1,digits-s+1):
        j=i+s
        #print(i,j)
        m1min[i,j],m1max[i,j]=MinandMax(i,j,ope,m1max,m1min)
        #print(MinandMax(i,j,ope,m1max,m1min))
        
print(m1max[1,-1])
#print(m1min)
##    
##for x in range (1,10,2):
##    print(x)
