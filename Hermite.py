import numpy as np
import matplotlib.pyplot as plt

def pochodna_stopnia_n(n, x, func):
    h = 1e-10
    xi = x
    for i in range(n+1):
        xi = (func(xi+h) - func(xi))/h
    return xi

def funkcja(x):
    return np.sin(x)

wezly = {0: [2,1],
         1: [4,-1],
         3: [5,-2]}

x_space = np.linspace(-1,4, 100)

'''def Hermite(x, wezly):
    suma = 0
    for i in range(len(wezly)+1):
        ai = pochodna_stopnia_n(i, x, funkcja)
        for j in range(i):
            ai *= (x-wezly[j])
        else:
            suma += ai
    else:
        return suma'''

def L(i, x):
    iloczyn = 1
    for j in range(len(wezly[list(wezly.keys())[0]])+1):
        if i != j:
            iloczyn *= (x - list(wezly.keys())[j])/(list(wezly.keys())[i] - list(wezly.keys())[j])
    else:
        return iloczyn

def L_prim(i):
    suma = 0
    for j in range(len(wezly[list(wezly.keys())[0]])+1):
        if i != j:
            suma += 1/(list(wezly.keys())[i] - list(wezly.keys())[j])
    else:
        return suma


def Ai(i, x):
    return (1 - 2*(x-list(wezly.keys())[i]) * L_prim(i))*(L(i, x))**2

def Bi(i, x):
    return (x - list(wezly.keys())[i])*(L(i, x))**2

def p(x, wezly: dict):
    suma = 0
    for i in range(len(wezly[list(wezly.keys())[0]])+1):
        suma += wezly[list(wezly.keys())[i]][0] * Ai(i, x) + wezly[list(wezly.keys())[i]][1] * Bi(i, x)
    else:
        return suma



interpolated = [p(x, wezly) for x in x_space]


plt.scatter(wezly.keys(), [wezly[i][0] for i in wezly.keys()])
plt.scatter(wezly.keys(), [wezly[i][1] for i in wezly.keys()])
plt.plot(x_space, interpolated, 'r')
#plt.plot(x_space, funkcja(x_space), 'b')
plt.show()
