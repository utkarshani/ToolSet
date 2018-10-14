import numpy as np
from scipy.linalg import solve

print "Linear Regression"
x=np.array([1,2,3,4])
y=np.array([2,4,6,8])

xi=np.array(sum(x))
print "Summation of xi =",xi

yi=np.array(sum(y))
print "Summation of yi =",yi

xi2sum=np.array(sum(np.square(x)))
print "Summation of xi square =",xi2sum

xiyisum=np.array(sum(np.multiply(x,y))) #dot product maybe in matrix, for a single vector maybe just multiply
print "Summation of dot product of xi and yi =",xiyisum

n=x.size
print "Summation of 1 or the size of the input vector =",n

A=np.array([(xi2sum,xi),(xi,n)]) 
print "Matrix A =", A

C=np.array([xiyisum,yi])
print "Matrix C =",C 

X=np.linalg.solve(A,C)
print "Solution of Ax = C; m(slope) and b(intercept)", X
print "where slope, m is", X[0] ,"and Intercept, b is", X[1]
