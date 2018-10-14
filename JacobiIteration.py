import numpy as np

A=np.array([[4,-1,0,1,0],[-1,4,-1,0,1],[0,-1,4,-1,0],[1,0,-1,4,-1],[0,1,0,-1,4]])
B=np.transpose(np.array([100,100,100,100,100]))
X=np.transpose(np.array([0,0,0,0,0]))

def Jacobian(A,B,X):
    for i in range (18):
        X=X+(B - np.dot(A,X))/np.diag(A) #R= B-np.dot(A,X), X=X+(R/np.diag(A))
    print "Jacobi Iteration Solution: ",X

Jacobian(A,B,X) 
