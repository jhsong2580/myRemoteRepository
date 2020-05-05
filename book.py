import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

def numerical_diff(f,x): #미분(수치미분)
    h=10e-50
    return (f(x+h)-f(x))/h 


def numerical_diff1(f,x):#미분(중심차분/중앙차분)
    h=1e-4
    return (f(x+h)-f(x-h))/2*h 

def function_1(x):
    return 0.01*x**2 + 0.1*x   #0.01x&2+0.1*x

def function_2(x):
    return x[0]**2 + x[1]**2  #x1^2 + x2^2

def numerical_gradient(f,x): #편미분
    h=1e-4 #0.0001
    grad = np.zeros_like(x)     #np.zeros_like(?) : Return an array of zeros with the same shape and type as a given array.
    
    for idx in range(x.size):
        tmp_val = x[idx]
        #f(x+h)계산
        #x : (x1,x2)
        x[idx]=tmp_val+h   #f(x1+h,x2)
        fxh1=f(x)

        #calculate f(x-h)
        x[idx]=tmp_val-h   #f(x1,x2+h)
        fxh2=f(x)

        grad[idx]=(fxh1-fxh2)/(2*h) # (f(x+h) - f(x-h))/2*h    <- 중앙차분  
        x[idx]=tmp_val
    return grad      #(f(x1+h,x2) - f(x1-h,x2))/2*h,(f(x1,x2+h) - f(x1,x2-h))/2*h

def numerical_gradient1(f, X):
    if X.ndim == 1:
        return numerical_gradient(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = numerical_gradient(f, x)
        
        return grad

if __name__ == '__main__':
    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25)
    X, Y = np.meshgrid(x0, x1)
    
    X = X.flatten()
    Y = Y.flatten()
    
    grad = numerical_gradient1(function_2, np.array([X, Y]) )
    
    plt.figure()
    plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")#,headwidth=10,scale=40,color="#444444")
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()