import matplotlib.pyplot as plt
import numpy as np
import random
def rd(A,B,C):
    [r1, r2] = np.random.random(2)
    x = np.sqrt(r1)
    return (1-x)*A+(x*(1-r2))*B+(x*r2)*C

A = np.array([0,0])
B = np.array([1,np.sqrt(3)])
C = np.array([2,0])

plt.plot(A[0],A[1],'ro',markersize=1)
plt.plot(B[0],B[1],'ro',markersize=1)
plt.plot(C[0],C[1],'ro',markersize=1)
M = rd(A,B,C)
plt.plot(M[0],M[1],'ro',markersize=0.3)
for i in range(25000):
    k = np.random.randint(3)
    #k = random.choices([0,1,2], weights=[0.1,0.45,0.45])[0]
    X = [A,B,C][k]
    I = (M+X)/2
    plt.plot(I[0],I[1],'bo',markersize=0.3)
    M = I
plt.show()
