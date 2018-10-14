import numpy as np

A=np.array([[4,-1,0,1,0],[-1,4,-1,0,1],[0,-1,4,-1,0],[1,0,-1,4,-1],[0,1,0,-1,4]])
B=np.transpose(np.array([100,100,100,100,100]))
X=np.transpose(np.array([0,0,0,0,0]))

def GaussSeidel(A,B,X):
    R=B-np.dot(A,X)
    for i in range(15):
        X=X+(R/np.diag(A))
        R=B-np.dot(A,X)
    print "Gauss Seidel Solution: ",X    

GaussSeidel(A,B,X)       