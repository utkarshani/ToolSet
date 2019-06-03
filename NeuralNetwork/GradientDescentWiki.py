import numpy as np

y_pred=np.array([14,16,18])
x=np.array([2,3,4])
w=np.transpose(np.ones((1,3), dtype=float))
b=np.ones((1,3),dtype=float)

def df(w):
    for i in range(0, len(y_pred)):
        tmp=2*(np.multiply((y_pred - (np.multiply(w,x) + b)),x))
    return tmp
    
def GradientDescent():
    cur_w = 0 # The algorithm starts at x=6
    gamma = 0.01 # step size multiplier
    precision = 0.00001
    previous_step_size = 1 
    max_iters = 10000 # maximum number of iterations
    iters = 0 #iteration counter
    
    #f(x)=(x^4)-3(x^3)+2
    #deriv=4(x^3) - 9(x^2)
    #df = lambda x: 4 * x**3 - 9 * x**2
    
    
        # df=lambda w: 2*((np.multiply((y_pred -(np.multiply(w,x) + b),x))))
    while (previous_step_size > precision and iters < max_iters):
        prev_w = cur_w
        cur_w -= gamma * df(prev_w)
        previous_step_size = abs(cur_w - prev_w)
        iters+=1
        
    print("The local minimum occurs at", cur_w)

GradientDescent()        