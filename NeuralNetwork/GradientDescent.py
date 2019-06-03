import numpy as np

#y=2x+10
# From calculation, it is expected that the local minimum occurs at x=9/4
def GradientDescent():
    cur_x = 6 # The algorithm starts at x=6
    gamma = 0.01 # step size multiplier
    precision = 0.00001
    previous_step_size = 1 
    max_iters = 10000 # maximum number of iterations
    iters = 0 #iteration counter
    
    #f(x)=(x^4)-3(x^3)+2
    #deriv=4(x^3) - 9(x^2)
    #df = lambda x: 4 * x**3 - 9 * x**2
    df = lambda x: 2*x
    
    while previous_step_size > precision and iters < max_iters:
        prev_x = cur_x
        cur_x -= gamma * df(prev_x)
        previous_step_size = abs(cur_x - prev_x)
        iters+=1
    
    print("The local minimum occurs at", cur_x)
    #The output for the above will be: ('The local minimum occurs at', 2.2499646074278457)
    
#y=2x+10
#x=np.array([1,2,3,4,5,6,7,8,9,10])
#y=np.array([12,14,16,18,20,])

GradientDescent()    