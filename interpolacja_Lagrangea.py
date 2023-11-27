import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return 1/(1+25*x**2)

def wierstras(x, a=0.9, b=((1+3*np.pi/2)/0.9 + 0.01)):
    suma = 0
    for n in range(100):
        suma += a**n * np.cos(b**n * np.pi * x)
    else:
        return suma

stopien = 100
wezly = [np.cos(((2*k - 1)*np.pi)/int(stopien*2)) for k in range(1,stopien+1)]
#wezly = np.linspace(-1,1,14)
x_space = np.linspace(-1,1,100)
y = np.array([func(x) for x in wezly])



def Lagrange_interpol(x, wezly, stopien):
    suma = 0
    for i in range(stopien+1):
        iloczyn = 1
        for j in range(stopien+1):
            if i != j:
                iloczyn *= (x-wezly[j])/(wezly[i]-wezly[j])
        else:
            suma += y[i] * iloczyn
    else:
        return suma

interpolated = np.array([Lagrange_interpol(x, wezly, len(wezly)-1) for x in x_space])
RMSE1 = np.sqrt(np.sum((np.array([func(x) for x in x_space]) - interpolated)**2))
#wierstras_interpolated = np.array([wierstras(x) for x in x_space])
#RMSE2 = np.sqrt(np.sum((np.array([func(x) for x in x_space]) - wierstras_interpolated)**2))


print(f'Lagrange: {RMSE1}')
#print(f'Wierstrass: {RMSE2}')
plt.scatter(wezly,y)
plt.plot(x_space, interpolated)
#plt.plot(x_space, wierstras_interpolated, 'y--')
plt.plot(x_space, func(x_space), 'r--')
plt.show()