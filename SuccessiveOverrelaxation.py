import numpy as np

A=np.array([[4,-1,0,1,0],[-1,4,-1,0,1],[0,-1,4,-1,0],[1,0,-1,4,-1],[0,1,0,-1,4]])
B=np.transpose(np.array([100,100,100,100,100]))
X=np.transpose(np.array([0,0,0,0,0]))

def SuccessiveOverrelaxation(A,B,X):
    R=B-np.dot(A,X)
    w=1.10
    for i in range(15):
        X=X+w*(R/np.diag(A))
        R=B-np.dot(A,X)
    print "Gauss Seidel Solution: ",X    

SuccessiveOverrelaxation(A,B,X)       