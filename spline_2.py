import numpy as np

data = np.array([[1.0, 3.0], [2.0, 1.0], [3.5,4.], [5., 0.], [6., 0.5], [9., -2.], [9.5, -3.0]])


def h(i):
    return data[i+1][0] - data[i][0]

def b(i):
    return (6/h(i)) * (data[i+1][1] - data[i][1])

def u(i):
    return 2*(h(i-1) + h(i)) - (h(i-1)**2)/h(i-1)

def v(i):
    if i == 0:
        return 0
    return b(i) - b(i-1) - h(i-1) * (v(i-1)/u(i-1))


def z(i):
    if i == 0 or i == len(data):
        return 0
    else:
        return (v(i) - h(i)*z(i+1))/u(i)

for i in range(8):
    try:
        print(z(i))
    except:
        print(f'couldnt print: {i}th')