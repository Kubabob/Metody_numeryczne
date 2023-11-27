import numpy as np

def f(x):
    return np.exp(x) - np.arctan(x)-2

def f_prim(x):
    h = 10e-10
    return (f(x) - f(x-h))/(h)



def newton_method(x_k, epsilon):
    if abs(f(x_k)) < epsilon:
        return x_k
    else:
        x_k1 = x_k - f(x_k)/f_prim(x_k)
        if abs(x_k1-x_k) < epsilon:
            return x_k1
        else:
            return newton_method(x_k1, epsilon)

print(newton_method(1, 10e-10))
