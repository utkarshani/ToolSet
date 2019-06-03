import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3]) #4,5,6,7,8,9,10,11,12,13,14,15]
#x=([1,2,3])
x=x.reshape(3,1)
#b=np.array([10,10,10])
y_pred=np.array([12,14,16]) #18,20,22,24,26,28,30,32,34,36,38,40]
w=np.ones((3,3), dtype=float)
#w=np.ndarray(shape=(1,1), dtype=float)
#w=[1]
#w=np.transpose(np.ones((1,3), dtype=float))
b=np.ones((1,3),dtype=float)
#y_pred=np.zeros((1,3),dtype=float)
error=0
deriv_b=0
deriv_w=0
            
def function(w,x,b):
    #y=2x+10
    #y=transpose(w)+b
    y_obs=(np.multiply(w,x) + b)
    #y_obs=activationFunction(y_obs)
    return y_obs
    
#Activation Functions
def sigmoid(Z):
    return 1/(1+np.exp(-Z))

def relu(Z):
    return np.maximum(0,Z)

def tanh(Z):
    #tmp = 1./(1+np.exp(-x))
    tmp = np.tanh(Z)
    return tmp

#Derivative of activation function
def sigmoid_derivative(Z):
    sig = sigmoid(Z)
    return sig * (1 - sig)

def relu_derivative(Z):
    #f'(x) = x > 0
    return np.greater(Z, 0).astype(int)
    
def tanh_derivative(Z):
    tmp = 1-np.tanh(Z)**2
    return tmp            

def errorFunction(y_pred,w,x,b):
    error=(y_pred-y_obs)**2
    return error
    # totalError=0
    # for i in range(0, len(y_pred)):
    #     totalError += (y_pred[i] - (y_obs[i])) ** 2
    # print("Error is: ",totalError)
    # return totalError #/ float(len(y_pred))
    
def errorFunctionDeriv_w(y_pred,w,x,b):
    deriv_w =-2*(sum(np.multiply((y_pred -(np.multiply(w,x) + b)),x)))
    return deriv_w
    
def errorFunctionDeriv_b(y_pred,w,x,b):
    deriv_b =-2*(sum((y_pred -(np.multiply(w,x) + b))))
    return deriv_b
    

def step_gradient(b_current, w_current, x, y_pred, learning_rate):
    #gradient descent
    # iters=100
    # for j in range(iters):
        b_gradient = 0
        w_gradient = 0
        N = float(len(x))
        for i in range(0, len(x)):
            b_gradient += -(2/N)*(sum((y_pred -(np.multiply(w,x) + b))))
            w_gradient += -(2/N)*(sum(np.multiply((y_pred -(np.multiply(w,x) + b)),x)))
        new_b = b_current - (learning_rate * b_gradient)
        new_w = w_current - (learning_rate * w_gradient) 
        return [new_b,new_w]


def gradient_descent_runner(x,y_pred, b_opt, w_opt, learning_rate, num_iteartions):
	b = b_opt
	w = w_opt
	for i in range(num_iteartions):
		b,w = step_gradient(b_opt, w_opt, x, y_pred, learning_rate)
	return [b,w]                

if __name__ == '__main__':
    #Define the dimensions for the input matrix, weight matrix and bais
    n=10
    m=10
    x=np.ones((m,n), dtype=float)
    w=np.ones((m,n), dtype=float)
    y_obs=function(w,x,b)
    user_activation=input("Enter the activation function. Enter the number: \n1)sigmoid  \n2)tanh \n3)Relu (Rectified Linear Unit) \n")
    print("User chose activation function- ",user_activation)
    if user_activation==1:
        act=sigmoid(y_obs)
    elif user_activation==2:
        act=tanh(y_obs)
    else:
        act=relu(y_obs)        
    #act=activationFunction(y_obs)
    error=errorFunction(y_pred,w,x,b)
    deriv_w=errorFunctionDeriv_w(y_pred,w,x,b)
    deriv_b=errorFunctionDeriv_b(y_pred,w,x,b)
    w_opt=0
    b_opt=0
    learning_rate=0.05
    iters=5000
    [final_b,final_w]=gradient_descent_runner(x,y_pred, b_opt, w_opt, learning_rate, iters)
    new_y_obs=function(final_w,x,final_b)
    print ("b is: ", final_b)
    print ("w is: ", final_w)
    plt.figure(1)
    plt.plot(x,y_pred,'bo')
    plt.plot(x,new_y_obs,'ro')
    plt.show()
