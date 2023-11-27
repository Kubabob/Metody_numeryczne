import numpy as np
import matplotlib.pyplot as plt

data = np.array([[0.0, 2.0, 1.0], [1.0, 4.0, -1.0], [3.0, 5.0, -2.0]]) #x, c_ij

c_i0 = [data[i][1] for i in range(len(data))]
c_i1 = [data[i][2] for i in range(len(data))]
x_1 = [data[i][0] for i in range(len(data))]

N = data.shape[0]
z = np.linspace(-1.0, 4.0, 100)

def l(x, i):
    iloczyn = 1
    for j in range(N):
        if i != j:
            iloczyn *= (x - x_1[j]) / (x_1[i] - x_1[j])
    else:
        return iloczyn


def derl(i):
    suma = 0
    for j in range(N):
        if i != j:
            suma += 1 / (x_1[i] - x_1[j])
    else:
        return suma


def A(i, x):
    return (1 - (2 * (x - x_1[i]) * derl(i))) * (l(x, i))**2


def B(i, x):
    return (x - x_1[i]) * (l(x, i))**2


def p(x):
    suma = 0
    for i in range(N):
        suma += c_i0[i] * A(i, x) + c_i1[i] * B(i, x)
    else:
        return suma


interpolated = [p(x) for x in z]

plt.plot(z, interpolated)
plt.plot(x_1, c_i0, 'o', color = 'red')
plt.plot(x_1, c_i1, 'o', color = 'magenta')
plt.show()

print(x_1)
print(c_i0)
print(c_i1)
print(interpolated)